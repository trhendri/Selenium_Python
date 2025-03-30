from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome()

driver.get('https://facebook.com')
driver.maximize_window()

#CSS_SELECTORS
# 1. tag and id  - tagname#valueofid
# 2. tag and class - tagname.valueofclass - tagname.valueofclass.valueofclass.valueofclass
# 3. tag and attribute - tagname[attribute=value] - no quotations
# 4. tag, class, and attribute -class -  tagname.classvalue[attribute=value] - id - tagname#idname[attribute=value]

#CSS_SELECTOR - tag and id - tagname#valueofID
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc')

#CSS_SELECTOR - tag and id - tagname.valueofclass
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext._55r1._6luy').send_keys('123@gmail.com')

#CSS_SELECTOR - tag and id - tagname[attribute = value]
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid=royal-email]').send_keys('emailemail@email.com')

#CSS_SELECTOR - tag, class/id, and attribute - tagname.classvalue[attribute=value]
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid=royal-pass]').send_keys('passwawa')
# time.sleep(3)

driver.find_element(By.CSS_SELECTOR, 'input#pass[data-testid=royal-pass]').send_keys('passwawa')
time.sleep(3)









driver.quit()