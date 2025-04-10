import pytest
from selenium import webdriver


"""

FIXTURES:

    Precondition
        Setup, Connection, API
        
    Test
    
    Test
    
    Assertion
    
    Postcondition
        clean, close, close


1. Arrange
2. Act
3. Assert
4. Cleanup


"""
driver = None

@pytest.fixture
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("close Browser")

def test_1(setup):
    driver.get("https://www.facebook.com")
    print("Test 1 executed")


def test_2(setup):
    driver.get("https://google.com")
    print("Test 2 executed")


def test_3(setup):
    driver.get("https://gmail.com")
    print("Test 3 executed")


