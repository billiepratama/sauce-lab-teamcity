import unittest
import pytest
from AppiumFrameWork.base.DriverClass import Driver

import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class test_ContactUsFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("App launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
