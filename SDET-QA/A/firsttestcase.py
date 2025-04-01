

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
import keyword
# print(keyword.kwlist)
# from selenium.webdriver.chrome.service import Service
# service_Object = Service()
#@pytest.fixture

driver = webdriver.Chrome()
#
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# driver.implicitly_wait(5)
#
# username_Field = driver.find_element(By.XPATH, '//input[@name="username"]')
# password_Field = driver.find_element(By.NAME, 'password')
# login_Button = driver.find_element(By.XPATH, '//button[@type="submit"]')
# username_Field.send_keys('Admin')
# password_Field.send_keys('admin123')
# login_Button.click()
#
# actual_Title = driver.title
# expected_title = "OrangeHRM"
#
# if actual_Title == expected_title:
#     print('Login Test Passed')
# else:
#     print("Login Test Failed")
#
# driver.close()

#Practice
driver.get('https://admin-demo.nopcommerce.com/login')
email = driver.find_element(By.CLASS_NAME, 'email')
password = driver.find_element(By.CLASS_NAME, 'password')
login = driver.find_element(By.CSS_SELECTOR, '.button-1')
email.clear()
email.send_keys('admin@yourstore.com')
driver.implicitly_wait(5)
password.clear()
password.send_keys('admin')
login.click()


driver.implicitly_wait(5)
page_actual_title = driver.title
page_expected_title = "Dashboard / nopCommerce administration"

if page_actual_title == page_expected_title:
    print('Login Test Passed')
else:
    print("Login Test Failed")
    print(driver.title)

driver.quit()