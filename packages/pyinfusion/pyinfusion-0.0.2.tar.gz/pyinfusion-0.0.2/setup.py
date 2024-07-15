from setuptools import setup, find_packages
import sys
import os

def key_authorization():
    access_key = os.getenv('ACCESS_KEY')
    if not access_key:
        print("ACCESS_KEY environment variable is not set.")
        sys.exit(1)

    if '--access-key' not in sys.argv:
        print("Access key is required to install this package.")
        sys.exit(1)
    
    access_key_index = sys.argv.index('--access-key') + 1
    if access_key_index >= len(sys.argv):
        print("Access key is required to install this package.")
        sys.exit(1)
    
    user_access_key = sys.argv[access_key_index]
    if user_access_key != access_key:
        print("Invalid access key.")
        sys.exit(1)
    
    sys.argv.remove('--access-key')
    sys.argv.pop(access_key_index - 1)

key_authorization()

setup(
    name='pyinfusion',
    version='0.0.2',
    packages=find_packages(),
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mobolaji Shobanke',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=['pyspark'],
    license='Proprietary License',
    license_files=['LICENSE']
)