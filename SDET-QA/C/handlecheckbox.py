from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC #for waits
from selenium.webdriver.support.wait import WebDriverWait #For Explicit Waits
import time
import pytest

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://testautomationpractice.blogspot.com/#')
driver.find_element(By.XPATH,'//input[@id="monday"]').click()
checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox" and @class="form-check-input"]')
# can also use like //input[@type='checkbox' and contains(@id,'day')]

for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)

#can use RANGE:
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#Select multiple checkboxes by choice
for checkbox in checkboxes:
    week_name = checkbox.get_attribute('id')
    if week_name == 'wednesday' or week_name == 'sunday':
        checkbox.click()


#select last 2 checkboxes of 7

for x in range(len(checkboxes) -2, len(checkboxes)): #range 5, 7
    checkboxes[x].click()

#select first two
for y in range(len(checkboxes)):
    if y<2:
        checkboxes[y].click()

#clear all checkboxes  if some are already selected
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


driver.quit()

