from time import sleep

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = ''
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('C:/Users/Billie Pratama/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn1"]')
ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
# ele_xpath = driver.find_element_by_xpath('//android.widget.Button[1]')
# ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@text="ENTER SOME VALUE"]')
ele_xpath.click()
sleep(2)
ele_xpath = driver.find_element_by_xpath('//android.widget.EditText').send_keys("Code2Lead")
sleep(2)