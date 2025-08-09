
from appium import webdriver
from appium.options.common import AppiumOptions
# It is recommended to run the Appium server automatically using AppiumService.
from appium.webdriver.appium_service import AppiumService
import time

#appium_service = AppiumService()
#appium_service.start()
#time.sleep(5)


# Define the desired capabilities for your test.
# This is a dictionary that tells Appium what device and app to test.
# You will need to change these values to match your specific device and app.
options = AppiumOptions()
appium_url = "http://127.0.0.1:4723"

launch = "android"
if launch == "browser":
    options.load_capabilities(
        {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "browserName": "Chrome",
            "appium:chromedriver_autodownload": True
        }
    )

elif launch == "ios":
    options.load_capabilities(
        {
            "platformName": "iOS",
            "platformVersion": "18.2",
            "automationName": "XCUITest",
            "bundleId": "com.example.apple-samplecode.UICatalog",
            "showXcodeLog": True
        }
    )
elif launch == "android":
    options.load_capabilities(
        {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'appPackage': 'io.appium.android.apis',
            'appActivity': '.ApiDemos'
        }
    )

# Create a new webdriver instance by connecting to the Appium server.
# The first argument is the URL of the Appium server.
# The second argument is the desired capabilities.
driver = webdriver.Remote(appium_url, options=options)

# You can now use the `driver` object to interact with your app.
# For example, you can open a URL in the browser:
#driver.get("https://www.google.com")

# When you are finished, you can close the session.
driver.quit()
# If you started the Appium server automatically, you should stop it.
#appium_service.stop()
