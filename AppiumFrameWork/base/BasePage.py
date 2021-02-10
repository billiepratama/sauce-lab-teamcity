import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.CustomLogger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        wait = WebDriverWait(self.driver, timeout=25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locatorValue)))
            return element
        else:
            self.log.info("Locator value " + locatorValue + "not found")

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locataorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue)
        except:
            self.takeScreenshot(locatorType)
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue : " + locatorValue)
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locataorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info("Clicked found with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue)
        except:
            self.takeScreenshot(locatorType)
            self.log.info(
                "Unable to click on element not found with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue)

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locataorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text on Element with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue)
        except:
            self.log.info(
                "Unable to send text on element not found with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locataorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Send text on Element with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue + " is displayed")
            return True
        except:
            self.log.info(
                "Unable to send text on element not found with LocatorType: " + locatorType + " with the locatorValue : " + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%h_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)
        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCodes(self, value):
        self.driver.press_keycode(value)
