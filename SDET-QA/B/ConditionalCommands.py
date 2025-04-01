from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()

#? 2. Conditional Commands
# is_displayed()
# is_enabled()
# is_selected() - radio and checkboxes

driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
print('Display Status:',search_box.is_displayed())

print('Enabled Status:', search_box.is_enabled())


male_radio = driver.find_element(By.XPATH, '//input[@id="gender-male"]')
female_radio = driver.find_element(By.XPATH, '//input[@id="gender-female"]')
male_radio.click()

print('Selected Status - M:', male_radio.is_selected())
print('Selected Status - F:', female_radio.is_selected())








driver.quit()