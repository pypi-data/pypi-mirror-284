# Pyinfusion
---
Pyinfusion calculates aggregated information about the Infusion and Active Time of Infusion pumps. Its inputs and outputs are spark dataframes. This package is developed solely for BD Alaris machines. Kindly note that the program is still under development and is undergoing experimentaion. It is not to be redistributed.




## How To Use
---

```python
from pyspark.sql import SparkSession
from pyinfusion import infusion_desc, infusion_maintenance_info

# create spark instance
spark = SparkSession.builder.appName('sample_app').getOrCreate()

# read in the data
infusion_data = spark.read.csv(filepath_infusion)
maintenance_data = spark.read.csv(filepath_maintenance)

# initilaze the package to obtain infusion time summary
infusion_inform = infusion_desc(data)

# obtain the infusion time summary
infusion_summary = infusion_inform.infusion_time()

# initialize package to obtain maintenance and infusion summary of equipement repaired
sample_summary = infusion_maintenance_info(infusion_summary, maintenance_data)

#obtain maintenance and infuion summary
pcu_summary = sample_summary.pcu_failure_time()
module_summary = sample_summary.module_failure_time()



```