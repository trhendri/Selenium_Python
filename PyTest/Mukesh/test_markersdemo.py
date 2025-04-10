import pytest

@pytest.mark.smoke
def test_login():
    print("Login done")


@pytest.mark.regression
def test_addProduct():
    print("add product")

@pytest.mark.smoke
def test_logout():
    print("Logout done")

