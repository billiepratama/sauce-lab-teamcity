from appium import webdriver

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = ''
# desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['app'] = ('C:/Users/Billie Pratama/Downloads/Android_Demo_App.apk')
# desired_caps['appPackage'] = 'com.code2lead.kwad'
# desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps['appiumVersion'] = "1.17.1"
caps['deviceName'] = "Google Pixel 3a XL GoogleAPI Emulator"
caps['deviceOrientation'] = "portrait"
caps['platformVersion'] = "10.0"
caps['platformName'] = "Android"
caps['app'] = "storage:filename=Android_Demo_App.apk"

url = "https://billiepratama:783c5dd338cc47dea51a1203d64f5a3e@ondemand.us-west-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(url, caps, keep_alive=True)


wait = WebDriverWait(driver, timeout=25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element_by_id("com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element_by_class_name("android.widget.EditText").send_keys("Code2Lead"))
driver.quit()


