from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC #for waits
from selenium.webdriver.support.wait import WebDriverWait #For Explicit Waits
import time
import pytest
from selenium.webdriver.support.select import Select #import Select Class


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

# driver.get('https://the-internet.herokuapp.com/basic_auth')

#? Inject username and password inside url
# https://username:password@website.com
# https://admin:admin@the-internet.herokuapp.com/basic_auth

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')











driver.quit()