import pytest


@pytest.fixture(scope='module')
def beforeClass():
    print("Before a Class")
    yield
    print("After Class")


@pytest.fixture()
def setUp():
    print("Before a Method")
    yield
    print("After method")


def test_methodA(beforeClass, setUp):
    print("This is method A")


def test_methodB(beforeClass, setUp):
    print("This is method B")
