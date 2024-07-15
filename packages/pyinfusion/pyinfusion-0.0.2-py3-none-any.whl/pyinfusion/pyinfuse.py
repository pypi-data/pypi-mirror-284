
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from itertools import chain
from pyspark.sql.window import Window
from pyspark.sql.types import *

import pandas as pd

class encoding_SM:
  def __init__(self, df):
    self.df = df.orderBy('InfusionID', 'StartTime')
    self.window_spec = Window.orderBy(col('InfusionID'), col('StartTime'))
    self.encode_df = self.encode()

  def encoding_single(self):
    # creating the dictionary of encodings
    encoding = {'Module Status Changed' : 2, 'Infusion Reprogrammed': -1,
                'Infusion Stopped': 1, 'Infusion Alarmed': 1,
                'Same Drug': -1, 'Infusion Paused': 1,
                'Weight Change': -1, 'Infusion Alerted': -1,
                'Drug Cancel': -1, 'Stop Secondary': -1,
                'Infusion Started': 0, 'Infusion Alert Resolved': -1,
                'Partial Dose': -1, 'Infusion Transitioned': 2
                }
    # creating the dictionary map
    encoding_map = create_map([lit(i) for i in chain(*encoding.items())])


    infusion = self.df.select(col('_PT'), col('InfusionID'),
              col('PCUSerialNumber'), col('ModuleSerialNumber'),
              col('DrugName'),
              col('InfusionProgramming'), col('StartTime'), col('StartReasonCode'),
              col('ActualDurationSeconds'), col('Alarm'), col('State'),
              col('InfusionType'), col('InfusionSetup'),
              col('Rate'), col('RateUnit'), col('ProgrammedDose')
              ).orderBy(
                  col('InfusionID'),
                  col('StartTime')
                  ).withColumn('EncodedStartReason',
                                encoding_map[col('StartReasonCode')]).select(col('_PT'), col('InfusionID'),
              col('PCUSerialNumber'), col('ModuleSerialNumber'),
              col('DrugName'),
              col('InfusionProgramming'), col('StartTime'), col('StartReasonCode'), col('EncodedStartReason'),
              col('ActualDurationSeconds'), col('Alarm'), col('State'),
              col('InfusionType'), col('InfusionSetup'),
              col('Rate'), col('RateUnit'), col('ProgrammedDose'))

    return infusion

  def encoding_multiple(self):
    def encoding_multi(df_spark, strt_reason: str, window_sp = self.window_spec):
      # create columns containing information from sliding window
      df_spark = (
          df_spark.withColumn('EncodedStartReason_prev', lag('EncodedStartReason', 1).over(window_sp))
                  .withColumn('EncodedStartReason_next', lead('EncodedStartReason', 1).over(window_sp))
      )

      df_spark = df_spark.withColumn(
          'EncodedStartReason', when( # instance for code: continuous
              (col('StartReasonCode') == strt_reason) &
              (col('EncodedStartReason_prev')== 0) &
                (col('EncodedStartReason_next').isin(-1, 1)), 2)
          .when( # instance for code: stop
              (col('StartReasonCode') == strt_reason) &
              ((col('EncodedStartReason_prev')== 0) | (col('EncodedStartReason_prev').isNull()))  &
              (col('EncodedStartReason_next').isin(-1, 1, 2) == False), 1
          ).when( # instace for code: start
              (col('StartReasonCode') == strt_reason) &
                  (col('EncodedStartReason_prev') != 0) &
                  (col('EncodedStartReason_next').isin(-1, 1)),
                  0).otherwise(col('EncodedStartReason'))
      )

      return df_spark


    df_encoded = self.encoding_single()

    multi = ['Infusion Delayed', 'Infusion Completed',
              'Infusion NEOI Started', 'Infusion Restarted',
              'Max Limit Reached', 'Infusion KVO Started']

    for k in range(len(multi)):
      for i_code in multi:
        df_encoded = encoding_multi(df_encoded, i_code)

    return df_encoded

  def encode(self):
    df_enc = self.encoding_multiple()

    state_encoding = {'Infusion Completed in KVO': 2,
                      'Infusion Delayed': 1, 'Infusion Idle': 1,
                      'Infusion Paused': 1, 'Non-Infusion Other': 1,
                      'Infusion Completed' : 1, 'Infusion Alarm': 1}
    # creating the dictionary map
    encoding_map_ = create_map([lit(i) for i in chain(*state_encoding.items())])

    df_enc = df_enc.withColumn(
        'EncodedStartReason', when(
            col('State').isin(*state_encoding.keys()), encoding_map_[col('State')]
        ).when(
            (col('EncodedStartReason').isNull()) & (col('State') == 'Infusing'), 2
            ).otherwise(col('EncodedStartReason'))
    ).drop('EncodedStartReason_prev', 'EncodedStartReason_next')

    return df_enc

class infusion_desc(encoding_SM):
  def __init__(self, df):
    # initialize parameters of parent class
    super().__init__(df)
    # obtain the list of unique infusion ids
    self.infusion_id = [i['InfusionID'] for i in self.encode_df.select('InfusionID').distinct().collect()]

  def row_detail(self):
    # obtain value of previous encoding
    data = self.encode_df.withColumn('EncodedStartReason_prev', lag('EncodedStartReason', 1).over(self.window_spec))

    # obtain the row number of each record to serve as index
    data = data.withColumn('row_number', row_number().over(self.window_spec))

    return data

  def inf_sum_encode(self):
    data_sum = self.row_detail()
    infusion_codes = self.infusion_id
    window_partition = self.window_spec.partitionBy('InfusionID')

    # obtain the minimum row number for each InfusionID
    data_sum = data_sum.withColumn('min_row_number', min('row_number').over(window_partition))

    # replace min row number with None
    data_sum = data_sum.withColumn('EncodedStartReason_prev',
                                   when((col('row_number') == col('min_row_number')),
                                        lit(None)).otherwise(col('EncodedStartReason_prev')))

    # drop the row_number and min_row_number
    data_sum = data_sum.drop('row_number', 'min_row_number')

    return data_sum

  def infusion_time(self):
    def infusion_length(df_data = self.inf_sum_encode()):
      # obtain the length of each infusion time in seconds
      df_data = df_data.withColumn(
          'StartTime_prev', lag('StartTime', 1).over(self.window_spec)
      )

      # carry out the substraction:
      df_data = df_data.withColumn(
          'infusion_time', when(
              (col('EncodedStartReason_prev').isin([0, 2])) &
              (col('EncodedStartReason').isin([-1,0,1,2])),
                (unix_timestamp(col('StartTime')) - unix_timestamp(col('StartTime_prev')))
              ).otherwise(lit(0))
      )

      return df_data

    infusion_info = infusion_length()

    # aggregate the data to find the summary of each infusionid
    infusion_info = infusion_info.groupBy('InfusionID',
                                          'PCUSerialNumber',
                                          'ModuleSerialNumber',
                                          ).agg(
                                              min('StartTime').alias('BOP_StartTime'),
                                              max('StartTime').alias('EOP_StartTime'),
                                              sum('infusion_time').alias('InfusionTime')
                                              ).withColumn(
                                                  'EqActiveTime', (unix_timestamp(col('EOP_StartTime')) - unix_timestamp(col('BOP_StartTime')))
                                              )

    return infusion_info

class infusion_maintenance_info:
  def __init__(self, infusion_df, maint_df):
    self.infusion_df = infusion_df
    self.maint_df = maint_df
    self.maint_equipment_serial = [i['Asset_Serial'] for i in self.maint_df.select('Asset_Serial').distinct().collect()]

  def pcu_repaired(self):
    # filter pcus present in maintenance df
    pcu_infusion_info = self.infusion_df.filter(col('PCUSerialNumber').isin(self.maint_equipment_serial))

    # reorder columns by pcu serial number
    pcu_infusion_info = pcu_infusion_info.select('PCUSerialNumber', 'BOP_StartTime', 'EOP_StartTime',
                                                 'InfusionTime', 'EqActiveTime')

    # obtain the PCU Serial Numbers
    pcu_serial = [i['PCUSerialNumber'] for i in pcu_infusion_info.select('PCUSerialNumber').distinct().collect()]

    return pcu_infusion_info

  def module_repaired(self):
    # filter modules present in maintenance df
    modules_infusion_info = self.infusion_df.filter(col('ModuleSerialNumber').isin(self.maint_equipment_serial))

    # reorder columns by module serial number
    modules_infusion_info = modules_infusion_info.select('ModuleSerialNumber', 'BOP_StartTime', 'EOP_StartTime',
                                                         'InfusionTime', 'EqActiveTime')

    # obtain the module serial numbers
    module_serial = [i['ModuleSerialNumber'] for i in modules_infusion_info.select('ModuleSerialNumber').distinct().collect()]

    return modules_infusion_info

  def maintenance_details(self, ext_df, column_name, window):

    @pandas_udf(IntegerType())
    def positive_difference(col_1:pd.Series, col_2:pd.Series) -> pd.Series:
      diff_series = (col_1 - col_2).dt.total_seconds()
      return diff_series.where(diff_series >= 0, None).astype('Int64')

    # obtain the maintenance information
    maintenance_df = self.maint_df

    # group the maintenance_df by the Asset_Serial
    maintenance_grouped = maintenance_df.groupBy('Asset_Serial').agg(collect_list('WO_Requested').alias('WO_timestamps'))

    # join external dataframe to grouped maintenance info
    ext_df = ext_df.join(maintenance_grouped, ext_df[column_name] == maintenance_grouped['Asset_Serial'], 'left')

    # explode the WO_timestamps column and find the shortest positive distnace
    ext_df = (
        ext_df.withColumn('explode_wo_timestamp', explode(col('WO_timestamps')))\
              .withColumn('time_diff', positive_difference(col('explode_wo_timestamp'), col('EOP_StartTime')))\
              .withColumn('min_time_diff', min('time_diff').over(window))
    )

    # calculate WO_Request time
    ext_df = ext_df.withColumn('WO_Requested', when((col('time_diff') == col('min_time_diff')),
                                                    col('explode_wo_timestamp')).otherwise(lit(None)))

    # remove null cases
    ext_df = ext_df.filter(col('WO_Requested').isNotNull())

    # aggregate the result
    ext_df = ext_df.groupBy(col(column_name), col('WO_Requested')).agg(
        min('BOP_StartTime').alias('ActiveStartTime'),
        max('EOP_StartTime').alias('ActiveStopTime'),
        sum('InfusionTime').alias('TotalInfusionTime'),
        sum('EqActiveTime').alias('TotalEqActiveTime')
        ).orderBy(column_name, 'WO_Requested')

    return ext_df

  def pcu_failure_time(self):
    # create the window
    pcu_window = Window.partitionBy(col('PCUSerialNumber'), col('BOP_StartTime'))

    # obtain the pcu information
    pcu_info = self.pcu_repaired()

    # calculate WO_Requested
    pcu_wo = self.maintenance_details(ext_df = pcu_info, column_name='PCUSerialNumber',
                                      window = pcu_window)

    # output result
    return pcu_wo

  def module_failure_time(self):
    # create the window
    module_window = Window.partitionBy(col('ModuleSerialNumber'), col('BOP_StartTime'))

    # obtain the module information
    module_info = self.module_repaired()

    # calculate WO_Requested
    module_wo = self.maintenance_details(ext_df = module_info, column_name='ModuleSerialNumber',
                                      window = module_window)

    # output result
    return module_wo