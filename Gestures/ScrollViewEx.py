from appium import webdriver
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

driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))').click()

driver.quit()