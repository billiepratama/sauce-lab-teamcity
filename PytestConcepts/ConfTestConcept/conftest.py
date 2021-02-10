import pytest


@pytest.fixture(scope='module')
def beforeClass():
    print("Before a Class")
    yield
    print("After Class")


@pytest.fixture()
def beforeMethod():
    print("Before a Method")
    yield
    print("After method")


def billie():
    print("Hello")
