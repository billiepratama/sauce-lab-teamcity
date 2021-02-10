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

element = driver.find_elements_by_class_name("android.widget.Button")
element[0].get_attribute()
for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

sleep(2)
driver.quit()
