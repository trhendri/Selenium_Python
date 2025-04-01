from imaplib import Commands

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.expected_conditions import title_is

driver = webdriver.Chrome()

#? 1. Application Commands
#
#? 2. Conditional Commands
#
#?  Browser Commands
#
#?  Navigational Commands
#
#?  Wait Commands




#? Application Commands
# title
# current_url
# page_source



driver.get('https://opensource-demo.orangehrmlive.com/')
print('Title:', driver.title)
print('Current URL: ', driver.current_url)
print('Page Source: \n ' ,  driver.page_source)

driver.quit()




