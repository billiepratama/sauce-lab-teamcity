import atexit

from appium import webdriver
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()
appium_service.start()  # Starts the appium client service


def stop_appium():
    print("Stop Appium")
    appium_service.stop()


atexit.register(stop_appium)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = ''
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('C:/Users/Billie Pratama/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
print("Text on the button ", ele_id.text)
ele_id.click()
