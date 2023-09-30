# LambdaTest Environment Check Tool

## Overview

The LambdaTest Environment Check Tool is a Python script designed to determine whether the conditions are met to utilize LambdaTest "Real Devices." 
It conducts checks for the availability of:
-specified uploaded apps, network-uploaded apps, and specified devices.

## Prerequisites

Before using this tool, ensure you have the following prerequisites:

- Python 3.x
- Required Python libraries: `requests`, `json`, `random`, `glob`, `os`, `time`, `string`

To install the necessary dependencies, you can use pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the **LamdaTest_Env_Check.py**, follow these steps:
1. **Upload your Application To LamdaTest-Platform**

   Documentation; https://www.lambdatest.com/support/docs/appium-java/

   Using App from local system:
   ```bash
   curl -u "LAMDATEST_USERNAME:LADMATEST_ACCESSKEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "appFile=@"/Users/user/path/to/APP_NAME.apk"" -F "name="APP_NAME""
   ```
   You will recevie the needed credentials for following variables:
   `app_id`, `app_url`, `app_name`, `app_type`, 
   These parameters are used to check *your* LamdaTest Environment 0-0

3. **Install requirements**

   Within your saved LamdaTest_Env_Check.py directory, open terminal and paste command:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set -credentials**

   You can easily set the credentials within LamdaTest_Env_Check.py:

   ```python
   LAMBDATEST_ACCESS_KEY = "LAMBDATEST_ACCESS_KEY_HERE"
   LAMBDATEST_USERNAME = "LAMBDATEST_USERNAME_HERE"
   BASE64_USERNAME_ACCESSKEY = "BASE64_USERNAME_ACCESSKEY_HERE"
   
   app_id = "UPLOADED_APP_ID_HERE"
   app_url = "UPLOADED_APP_URL_HERE"
   app_name = "UPLOADED_APP_NAME_HERE"
   app_type = "APP_TYPE_HERE"

   # Define the .json file available devices output directory:
   directory_path = "/Users/user/path/to/LamdaTest_Env_Check_results"
   
   # Define the "Real Devices" names we want to utilize
   real_device_name_01 = "Galaxy S23 Ultra"
   real_device_name_02 = "Galaxy S23 Ultra"
   real_device_name_03 = "Poco X3 Pro"
   real_device_name_04 = "Poco M4 Pro"
   real_device_name_05 = "Pixel 7"
   real_device_name_06 = "Pixel 7 Pro"
   ```
   

