import requests
import json
import string
import os
import random
import glob
import time



# This function is designed and will be utilized to check if the conditions are met to utilise LamdaTest "Real Devices" .
# We will check three main things;
# Specified Uploaded-App availability
# Specified Network Uploaded-App availability
# Specified Device'(s) availability

# Define color codes, utilise to print colored-text
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    CYAN = '\033[96m'
    BLACK = '\033[30m'  # Black text


def check_lambdatest_environment():

    # Define your LambdaTest credentials
    LAMBDATEST_ACCESS_KEY = "LAMBDATEST_ACCESS_KEY_HERE"
    LAMBDATEST_USERNAME = "LAMBDATEST_USERNAME_HERE"
    BASE64_USERNAME_ACCESSKEY = "BASE64_USERNAME_ACCESSKEY_HERE"

    # Define application to utilize from uploaded applications to LamdaTest-platform (and check availability ofc)
    app_id = "UPLOADED_APP_ID_HERE"
    app_url = "UPLOADED_APP_URL_HERE"
    app_name = "UPLOADED_APP_NAME_HERE"
    app_type = "APP_TYPE_HERE"

    # Define the "Real Devices" names we want to utilise (and check availability ofc)
    real_device_name_01 = "Galaxy S23 Ultra"
    real_device_name_02 = "Galaxy S23 Ultra"
    real_device_name_03 = "Poco X3 Pro"
    real_device_name_04 = "Poco M4 Pro"
    real_device_name_05 = "Pixel 7 "
    real_device_name_06 = "Pixel 7 Pro"

    # Construct the authentication header
    auth_header = (LAMBDATEST_USERNAME, LAMBDATEST_ACCESS_KEY)

    # Define the URL's for the LambdaTest API endpoint (we use ofc):
    devices_available_url = "https://mobile-api.lambdatest.com/mobile-automation/api/v1/list?region=us" # Available devices (us)
    uploaded_app_available_url = "https://manual-api.lambdatest.com/app/data?type=android&level=user" # Uploaded app-status
    network_app_available_url = "https://mobile-api.lambdatest.com/mobile-automation/api/v1/fetchpatchedapkurl" # Network uploaded app-status

    # Define the .json file available devices output directory:
    directory_path = "/Users/user/path/to/LamdaTest_Env_Check_results"


    # Send the first authenticated GET request using requests library
    print(f"{colors.BLUE}Sending requests for the devices available-devices LamdaTest live data...{colors.END}")
    print(f"{colors.RED}Currently requesting status for following Devices;{colors.END}")
    print(f"{colors.GREEN}Device; '{real_device_name_01}' {colors.END}")
    print(f"{colors.GREEN}Device; '{real_device_name_02}' {colors.END}")
    print(f"{colors.GREEN}Device; '{real_device_name_03}' {colors.END}")
    print(f"{colors.GREEN}Device; '{real_device_name_04}' {colors.END}")
    print(f"{colors.GREEN}Device; '{real_device_name_05}' {colors.END}")
    print(f"{colors.GREEN}Device; '{real_device_name_06}' {colors.END}")

    devices_available_response = requests.get(devices_available_url, auth=auth_header)

    # Check the response status code
    if devices_available_response.status_code == 200:
        # Request was successful, you can process the response content here
        data_available_devices = devices_available_response.json()
        # print(data_available_devices)
        devices_available_successful_response = True
    else:
        # Request failed, handle the error
        devices_available_successful_response = False
        print(f"Request failed with status code {devices_available_response.status_code}")
        print(devices_available_response.text)


    # Send the second authenticated GET request using requests library
    print(f"{colors.BLUE}Sending requests for the specified available-uploaded-application'(s) LamdaTest live data...{colors.END}")
    uploaded_app_available_response = requests.get(uploaded_app_available_url, auth=auth_header)

    # Check the response status code
    if uploaded_app_available_response.status_code == 200:
        # Request was successful, you can process the response content here
        data_available_uploaded_app = uploaded_app_available_response.json()
        # print(data_available_uploaded_app)
        uploaded_app_available_successful_response = True
    else:
        # Request failed, handle the error
        uploaded_app_available_successful_response = False
        print(f"Request failed with status code {uploaded_app_available_response.status_code}")
        print(uploaded_app_available_response.text)

    # Define the headers including the Authorization header for uploaded-app LamdaTest-servers
    headers = {
        "Authorization": f"Basic {BASE64_USERNAME_ACCESSKEY}",   # This is a Base64-encoded string that includes your username and API access key. The format is Basic username:access_key
        "Content-Type": "application/json"
    }

    # Define the JSON payload
    payload = {
        "appId": app_id
    }

    # Send the third GET request with headers and payload for network-status uploaded app
    print(f"{colors.BLUE}Sending requests for status of available-network-connection specified uploaded application LamdaTest live data...{colors.END}")
    print(f"{colors.RED}Currently requesting network-status for following uploaded-application;{colors.END}")
    print(f'{colors.GREEN}"app_id":"{app_id}","name":"{app_name}","type":"{app_type}","app_url":"{app_url}"{colors.END}')
    print(f'{colors.GREEN}"url":"htps://prod-falcon-lt-app-artefacts-v1.s3-accelerate.amazonaws.com/prod/1520084/2023/09/26/boltmirrorappapk-1695688505434.apk","custom_id":null{colors.END}')
    network_app_available_response = requests.post(network_app_available_url, headers=headers, json=payload)

    # Check the response status code
    if network_app_available_response.status_code == 200:
        # Request was successful, you can process the response content here
        data_network_app_available = network_app_available_response.json()
        # print(data_network_app_available)
        network_app_available_successful_response = True
    else:
        # Request failed, handle the error
        print(f"Request failed with status code {network_app_available_response.status_code}")
        print(network_app_available_response.text)
        network_app_available_successful_response = False


    # Now we will parse the data from the first request, available uploaded-app "data_available_uploaded_app".
    if uploaded_app_available_successful_response == True:

        # Initialize a dictionary to store app availability
        app_availability = {app_id: False}

        # Loop through the listed apps in the response
        for app in data_available_uploaded_app["data"]:
            if app["app_id"] == app_id and app["name"] == app_name and app["type"] == app_type:
                app_availability[app_id] = True
                print(f"{colors.YELLOW}----------------------------------------------------------------------------------------LIVE DATA REQUEST--------------------------------------------;;;;------{colors.END}")
                print(f"{colors.YELLOW}--------------------------------------------------------------- ----------------------------RESULTS--------------------------------------------------;;;;------{colors.END}")
                print(f"{colors.RED}Live Available Specified LamdaTest Uploaded-App; {colors.END}{colors.YELLOW}'{app_name}',{colors.END}{colors.RED};{colors.END}")
                print(f"{colors.GREEN}app_name;'{app_name}', is present and available{colors.END}")
                print(f"{colors.GREEN}app_id; '{app_id}', is present and available{colors.END}")
                print(f"{colors.GREEN}app_type; '{app_type}' is present and available{colors.END}")
                print(f"{colors.GREEN}app_url; '{app_url}'is present and available{colors.END}")


                app_availability[app_id and app_name and app_type] = True     # Specifies which uploaded-applications are available at this time (in data)


        # Check if the specified app is not available
        if not app_availability[app_id and app_name and app_type]:
            print(f"{colors.BLUE}The specified app is currently not available{colors.END}")
            app_availability[app_id and app_name and app_type] = False

    else:
        print(f"{colors.BLUE}Request failed with status code {data_available_uploaded_app.status_code}{colors.END}")

    # Now we will parse the data from the second request, available network for uploaded app "data_network_app_available".
    if network_app_available_successful_response == True:

        # Initialize a variable to store network status
        network_status = data_network_app_available["data"].get("patched_url")

        # Check if "patched_url" is present within "data" array, this indicates network is up and running for specified app.
        if network_status:
            print(f"{colors.RED}Live Available LamdaTest Uploaded-App; {colors.END}{colors.YELLOW}'{app_name}',{colors.END}{colors.RED} Network Status;{colors.END}")
            print(f"{colors.GREEN}app_name;'{app_name}', network is present and available{colors.END}")
            network_status = True

        else:
            print(f"{colors.BLUE}Patched URL is not available, network connection may not be working.{colors.END}")
            network_status = False

    else:
        print("Data key is not present in the response.")
        network_status = False


    # Now we will parse the data from the third request, available devices "data_available_devices".
    if devices_available_successful_response == True:
        # Names of devices to check for, there presents in the returned data array.
        devices_to_check = [real_device_name_01, real_device_name_02, real_device_name_03, real_device_name_04, real_device_name_05, real_device_name_06]    # Defined earlier in code, simply the names of real devices

        # Initialize a dictionary to store device availability
        device_availability = {}

        # Loop through the listed devices in the response
        print(f"{colors.RED}Live Available LambdaTest 'Real Devices':{colors.END}")
        for device in data_available_devices:
            device_name = device['deviceName']  # Get the device name
            platform_version = device['platformVersion']  # Get the platform version

            # Check if the device is in the list of devices to check
            if device_name in devices_to_check:
                print(
                    f"{colors.GREEN}Device; '{device_name}' is present and available.       Device OS; {platform_version}{colors.END}")

                # Create a nested dictionary to store availability and platform version
                device_info = {'available': True, 'platform_version': platform_version}

                # Add the device info to the device_availability dictionary
                device_availability[device_name] = device_info

        # Check if all specified devices are not available
        if all(not device_info['available'] for device_info in device_availability.values()):
            print(f"{colors.BLUE}All specified devices are currently not available{colors.END}")

    else:
        print(
            f"{colors.BLUE}Request failed to send with status code {devices_available_response.status_code}{colors.END}")

    if all([device_availability[real_device_name_01] or device_availability[real_device_name_02] or device_availability[real_device_name_03] or device_availability[real_device_name_04] or device_availability[real_device_name_05] or device_availability[real_device_name_06], app_availability[app_id and app_name and app_type], network_status]):    # If all three necessary dependencies are met (so  == True), we take action!
        print(f"{colors.CYAN}--------------------------------------------------------------------------- {colors.END}")
        print(f"{colors.CYAN}All conditions are met. Ready to spin-up wanted available 'Real Device'! {colors.END}")
        print(f"{colors.CYAN}Specified Uploaded-App;{colors.YELLOW}'AVAILABLE',{colors.END} {colors.END}")
        print(f"{colors.CYAN}Specified Network Uploaded-App;{colors.YELLOW}'AVAILABLE',{colors.END} {colors.END}")
        print(f"{colors.CYAN}Specified Device'(s);{colors.YELLOW}'AVAILABLE',{colors.END} {colors.END}")

    else:
        print("Not all conditions are met. Please check above terminal error logs")


    # Choose a random available device and its platform version
    random_device = None
    platform_version = None
    available_devices = {device: info for device, info in device_availability.items() if info['available']}
    if available_devices:
        random_device = random.choice(list(available_devices.keys()))
        platform_version = available_devices[random_device]['platform_version']

    # Check if a random device is available
    if random_device and platform_version:
        print(f"{colors.CYAN}--------------------------------------------------------------------------- {colors.END}")
        print(f"{colors.CYAN}Successfully saved current random chosen {colors.END}{colors.YELLOW}available{colors.END}{colors.CYAN} data/info{colors.END}")
        print(f"{colors.CYAN}needed for spinning up device; {colors.END}{colors.BLUE}'{random_device}'{colors.END} ")

    else:
        print("No available devices within 'available_devices' dictionary.")

    # json, file structure we utilise for fetching current live available devices.
    capability = {
        "platformName": "android",
        "deviceName": "{device_name_variable}",
        "platformVersion": "{platform_version_variable}",
        "app": "{app_url_variable}",
        "devicelog": True,
        "visual": True,
        "network": True,
        "video": True,
        "build": "{device_name_variable}",
        "name": "{device_name_variable}",
        "project": "project-goodluck!",
        "deviceOrientation": "portrait",
        "geoLocation": "US",
        "language": "en",
        "locale": "en",
        "idleTimeout": 600,
        "isRealMobile": True
    }



    # Replace placeholders with actual values
    capability["deviceName"] = random_device
    capability["platformVersion"] = platform_version
    capability["app"] = app_url
    capability["build"] = random_device
    capability["name"] = random_device

    # Generate a timestamp to include in the file name
    current_date = time.strftime("%Y_%m_%d%")
    current_time = time.strftime("%H:%M:%S")


    # Create the file name with the timestamp which will store Available LamdaTest Devices!
    file_name = f"output_available_devices_{current_date}_{current_time}{''.join(random.choice(string.ascii_letters) for _ in range(2))}.json"

    # Create the full file path
    file_path = os.path.join(directory_path, file_name)

    # Create the JSON file with the modified capability structure
    with open(file_path, 'w') as json_file:
        json.dump(capability, json_file, indent=4)

    # Print the generated file name
    print(f"{colors.CYAN}Saved Within JSON file; {colors.CYAN}{colors.RED}'{file_name}'{colors.END}")

    # Now you can cat out the created JSON file to the terminal
    with open(file_path, 'r') as json_file:
        json_content = json_file.read()
        print(f"{colors.RED}JSON Content:{colors.END}")
        print(f"{colors.CYAN}{json_content}{colors.END}")

check_lambdatest_environment()


def fetch_available_devices():
    # Function to find the name of the most recently created json file for available-devices.
    # This has the most recent/live data fetched for available devices on the LamdaTest platform
    # This function is lightening-fast! So we can call it whenever within the code.

    # Specify the directory path
    directory_path = "/Users/user/path/to/LamdaTest_Env_Check_results"

    # List all JSON files in the directory
    json_files = glob.glob(os.path.join(directory_path, "*.json"))

    # Sort the list by modification time (most recent first)
    json_files.sort(key=os.path.getmtime, reverse=True)

    # Get the most recently created JSON file
    if json_files:
        most_recent_json_file = json_files[0]
        file_name = os.path.basename(most_recent_json_file)
        print(f"{colors.YELLOW}Most Recently Created JSON File:{colors.END}, {colors.RED}'{file_name}'{colors.END}")
        print(f"{colors.YELLOW}This File Stores Live Available Devices,{colors.END} {colors.RED}*all needed information*{colors.END}{colors.CYAN}")

        # Now you can use most_recent_json_file or file_name as needed
    else:
        print(f"No JSON files found in the directory {directory_path}.")

fetch_available_devices()

