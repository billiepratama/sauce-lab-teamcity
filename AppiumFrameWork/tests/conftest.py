from time import sleep

import pytest
from AppiumFrameWork.base.DriverClass import Driver


@pytest.fixture(scope='class')
def beforeClass(request):
    print("Hello")
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    print("Before a Class")
    yield driver
    sleep(5)
    driver.quit()
    print("After Class")


@pytest.fixture()
def beforeMethod():
    print("Before a Method")
    yield
    print("After method")


def billie():
    print("Hello")
