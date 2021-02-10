# 1. Import the files
import unittest
from AppiumFrameWork.tests.test_LoginTest import test_LoginTest
from AppiumFrameWork.tests.test_ContactUsFormTest import test_ContactUsFormTest

# 2. Create the object of the class using unitTest

cf = unittest.TestLoader().loadTestsFromTestCase(test_ContactUsFormTest)
gt = unittest.TestLoader().loadTestsFromTestCase(test_LoginTest)
# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf, gt])
# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)
