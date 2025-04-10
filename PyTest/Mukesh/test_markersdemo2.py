import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login done")


@pytest.mark.skipif(sys.version_info<3,9, reason="Python version not supported")
def test_addProduct():
    print("add product")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout done")

@pytest.mark.parametrize
def test_closeApplication():
    assert True
    print("close the application")