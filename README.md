# LambdaTest Environment Check Tool

## Overview

The LambdaTest Environment Check Tool is a Python script designed to determine whether the conditions are met to utilize LambdaTest "Real Devices." It conducts checks for the availability of specified uploaded apps, network-uploaded apps, and specified devices.

Not only will we print LamdaTest platform availability within Terminal-window. We will also ouput a .json-file containing recently fetched *available-devices*. *0-0*


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
   

2. **Install requirements**

   Within your saved LamdaTest_Env_Check.py directory, open terminal and paste command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set -credentials**

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

4. **Run LamdaTest_Env_Check.py**
   ```bash
   python3 LamdaTest_Env_Check.py
   ```

## Ouput 
```bash
 Sending requests for the devices available-devices LambdaTest live data...
 Currently requesting status for the following Devices:
 Device: 'Huawei P20 Pro'
 Device: 'Huawei P30'
 Device: 'Huawei P30 Pro'
 Device: 'Huawei Mate 20 Pro'
 Device: 'Oppo A15'
 Device: 'Oppo F17'

 Sending requests for the specified available-uploaded-application'(s) LambdaTest live data...
 Sending requests for status of available-network-connection specified uploaded application LambdaTest live data...

 Currently requesting network-status for the following uploaded-application:
 "app_id":"APP101605731695688506635546","name":"bolt-mirror-appv1","type":"android",
 "app_url":"lt://APP101605731695688506635546"
 "url":"https://prod-falcon-lt-app-artefacts-v1.s3-accelerate.amazonaws.com/prod/1520084/2023/09/26/boltmirrorappapk-    
 1695688505434.apk",
 custom_id:null

 -----------------------------LIVE DATA REQUEST----------------------------------------
 ----------------------------------RESULTS---------------------------------------------
 Live Available Specified LambdaTest Uploaded-App: 'bolt-mirror-appv1',
 app_name: 'bolt-mirror-appv1', is present and available
 app_id: 'APP101605731695688506635546', is present and available
 app_type: 'android' is present and available
 app_url: 'lt://APP101605731695688506635546' is present and available

 Live Available LambdaTest 'Real Devices':
 Device: 'Oppo A15' is present and available.       Device OS: 10
 Device: 'Huawei P30' is present and available.       Device OS: 10
 Device: 'Huawei P30 Pro' is present and available.       Device OS: 10
 Device: 'Huawei P20 Pro' is present and available.       Device OS: 10
 Device: 'Oppo F17' is present and available.       Device OS: 10
 --------------------------------------------------------------------------- 
 All conditions are met. Ready to spin-up the wanted available 'Real Device'! 
 Specified Uploaded-App: 'AVAILABLE', 
 Specified Network Uploaded-App: 'AVAILABLE', 
 Specified Device(s): 'AVAILABLE', 
 --------------------------------------------------------------------------- 

 Successfully saved the current randomly chosen available data/info
 needed for spinning up the device: 'Huawei P30 Pro' 
 Saved Within JSON file: 'output_available_devices_2023_09_30%_01:34:42uC.json'

 JSON Content:
 {
     "platformName": "android",
     "deviceName": "Huawei P30 Pro",
     "platformVersion": "10",
     "app": "lt://APP101605731695688506635546",
     "devicelog": true,
     "visual": true,
     "network": true,
     "video": true,
     "build": "Huawei P30 Pro",
     "name": "Huawei P30 Pro",
     "project": "project-bolt",
     "deviceOrientation": "portrait",
     "geoLocation": "NL",
     "location": {
         "lat": "52.3791283",
         "long": "4.900272"
     },
     "language": "en",
     "locale": "en",
     "idleTimeout": 2700,
     "isRealMobile": true
 }

 Most Recently Created JSON File: 'output_available_devices_2023_09_30%_01:34:42uC.json'
 This File Stores Live Available Devices, *all needed information*
```
## Blessed 0-0
```---```
Don't worry the ouput is more colorfull on the real terminal. YnotY2 



   


