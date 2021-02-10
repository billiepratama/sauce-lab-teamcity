from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = ''
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('C:/Users/Billie Pratama/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, timeout=25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element_by_android_uiautomator('text("ScrollView")'))
ele.click()

print("Device width and height : ", driver.get_window_size())
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

# Top to bottom
startx = screenWidth/2
endx = screenWidth/2
starty = screenHeight*8/9
endy = screenHeight/9


# Bottom to top
startx2 = screenWidth/2
endx2 = screenWidth/2
starty2 = screenHeight/9
endy2 = screenHeight*8/9

sleep(2)
actions = TouchAction(driver)
actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
sleep(4)
actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()
driver.quit()