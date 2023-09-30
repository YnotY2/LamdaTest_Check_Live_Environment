LambdaTest Environment Check Tool

This Python script is designed to check if the conditions are met to utilize LambdaTest "Real Devices." It performs checks for the availability of specified uploaded apps, network-uploaded apps, and specified devices.

Prerequisites:

Before running this tool, ensure you have the following prerequisites:

- Python 3.x
- Required Python libraries: `requests`, `json`, `random`, `glob`, `os`, `time`, `string` 

To install the required dependencies, you can use pip:

pip install -r requirements.txt

Usage:

1. Clone the repository or download the script.

2. Open the script and replace the following placeholders with your LambdaTest credentials and app/device information:

   LAMBDATEST_ACCESS_KEY = "LAMBDATEST_ACCESS_KEY_HERE"
   LAMBDATEST_USERNAME = "LAMBDATEST_USERNAME_HERE"
   BASE64_USERNAME_ACCESSKEY = "BASE64_USERNAME_ACCESSKEY_HERE"
   
   app_id = "UPLOADED_APP_ID_HERE"
   app_url = "UPLOADED_APP_URL_HERE"
   app_name = "UPLOADED_APP_NAME_HERE"
   app_type = "APP_TYPE_HERE"
   
   # Define the "Real Devices" names we want to utilize
   real_device_name_01 = "Galaxy S23 Ultra"
   real_device_name_02 = "Galaxy S23 Ultra"
   real_device_name_03 = "Poco X3 Pro"
   real_device_name_04 = "Poco M4 Pro"
   real_device_name_05 = "Pixel 7"
   real_device_name_06 = "Pixel 7 Pro"

3. Save the changes.

4. Run the script using Python:

   python LamdaTest_Env_Check.py

The script will perform checks for the availability of uploaded apps, network-uploaded apps, and specified devices on the LambdaTest platform. It will print the results to the terminal.

Output:

The script generates JSON files containing information about available devices. You can find the most recently created JSON file in the specified directory.

To fetch the name of the most recently created JSON file, you can use the `fetch_available_devices()` function within the script.

