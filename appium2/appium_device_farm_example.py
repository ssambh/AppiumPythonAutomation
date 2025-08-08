import os
from appium import webdriver
from appium.options.common import AppiumOptions

# In AWS Device Farm, the Appium server URL is not hardcoded.
# It is provided by the Device Farm environment.
# We will leave the URL as a placeholder, as it will be overridden by Device Farm.
url = "http://127.0.0.1:4723"

# The desired capabilities will be set dynamically based on the
# environment variables provided by AWS Device Farm.
options = AppiumOptions()
options.load_capabilities({
    "platformName": os.environ.get("DEVICEFARM_DEVICE_PLATFORM_NAME"),
    "platformVersion": os.environ.get("DEVICEFARM_DEVICE_OS_VERSION"),
    "deviceName": os.environ.get("DEVICEFARM_DEVICE_NAME"),
    # The app path is also provided by Device Farm.
    # You will need to upload your app to a Device Farm project.
    "app": os.environ.get("DEVICEFARM_APP_PATH"),
    # You can add other capabilities as needed.
})

# When running in AWS Device Farm, the webdriver.Remote instance
# will be created with the correct Appium server URL.
driver = webdriver.Remote(url, options=options)

# Your test code remains the same.
driver.get("https://www.google.com")

driver.quit()
