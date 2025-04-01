from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()

#? Text vs Get Attribute
#  clear()
# .text
# .get_attribute('value')

driver.get('https://admin-demo.nopcommerce.com/login')

email_field = driver.find_element(By.XPATH, '//input[@id="Email"]')
email_field.clear()
email_field.send_keys('abc123')
time.sleep(2)



print('Result of Text: ', email_field.text) #returns nothing
print('Result of get_attribute:', email_field.get_attribute('value')) #returns 'abc123' and input text, id, value, class, name etc

login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print('Button Text:', login_button.text)


driver.quit()
