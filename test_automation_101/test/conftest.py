import pytest
from selenium import webdriver

#must create in conftest.py to use fixtures

@pytest.fixture()
def chrome():
    #initialize a chrome driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option(name='excludeSwitches', value= ['enable-logging'])  
    driver = webdriver.Chrome(options)

    #provide the driver instance to the test function
    #and allows for tear down after test function completed
    yield driver

    #teardown
    driver.quit()

# def firefox():
#     #initialize firefox driver
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     yield driver
#     driver.quit()