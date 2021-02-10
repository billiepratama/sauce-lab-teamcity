import unittest
import pytest

import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.LoginPage import LoginPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class test_LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        print("Testttttt")
        # self.gt = LoginPage(self.driver)
    #     self.bp = BasePage(self.driver)
    #
    @pytest.mark.run(order=5)
    def test_enterDataInEditBox(self):
        print("Hello")
    #     self.gt.enterText()
    #     self.gt.clickOnSubmit()
    #
    # @pytest.mark.run(order=4)
    # def test_openLoginScreen(self):
    #     cl.allureLogs("App Opened")
    #     self.bp.keyCodes(4)
    #     self.gt.clickLoginButton()
    #     self.gt.enterEmail()
    #     self.gt.enterPassword()
    #     self.gt.clickOnLoginB()
    #     self.gt.verifyAdminScreen()
    #
    # @pytest.mark.run(order=3)
    # def test_loginFailMethod(self):
    #     cl.allureLogs("App Opened")
    #     self.gt.clickLoginButton()
    #     self.gt.enterEmail()
    #     self.gt.enterPassword2()
    #     self.gt.clickOnLoginB()
    #     self.gt.verifyAdminScreen()
