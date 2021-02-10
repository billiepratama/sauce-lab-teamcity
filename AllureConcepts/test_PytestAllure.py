import pytest
import allure


def test_methodA():
    allureLogs("Launching App")
    allureLogs("This is a Method A step-1")
    allureLogs("This is a Method A step-2")
    print("This is method A")


@pytest.mark.skip
def test_methodB():
    print("This is method B")


def test_methodC():
    print("This is method C")


def test_methodD():
    print("This is method D")
    assert False


def allureLogs(text):
    with allure.step(text):
        pass

