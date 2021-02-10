from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = ''
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('C:/Users/Billie Pratama/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele_text = driver.find_element_by_android_uiautomator('new UiSelector().text("ENTER SOME VALUE")')
ele_text = driver.find_element_by_android_uiautomator('text("ENTER SOME VALUE")')
ele_text.click()
ele_text.