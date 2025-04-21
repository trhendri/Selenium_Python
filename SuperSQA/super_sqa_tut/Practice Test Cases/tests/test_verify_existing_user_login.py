from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest





# - Register a user so can be used for the test
# - Go to my account page directly
# - Fill in the login form
# - Verify user is logged in

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://demostore.supersqa.com/my-account/")

    yield driver
    driver.quit()

test_email_address = "testesttestemamailil@email.com"
test_password = "TestPassword123!!"

def test_new_user_registration(driver):

    register_email_field = driver.find_element(By.ID, "reg_email")
    register_password_field = driver.find_element(By.ID, "reg_password")
    register_button = driver.find_element(By.XPATH, "//button[@name='register']")

    register_email_field.click()
    register_email_field.clear()
    register_email_field.send_keys(test_email_address)
    register_password_field.click()
    register_password_field.clear()
    register_password_field.send_keys(test_password)
    register_button.click()
    my_account_url = driver.current_url

    assert driver.current_url == my_account_url

def test_verify_existing_user_login(driver):
    driver.get("http://demostore.supersqa.com/my-account/")
    login_email_field = driver.find_element(By.ID, "username")
    login_password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@name='login']")

    login_email_field.clear()
    login_email_field.send_keys(test_email_address)
    login_password_field.clear()
    login_password_field.send_keys(test_password)

    successful_login_heading_text = "My account"

    successful_login_heading = driver.find_element(By.CSS_SELECTOR, ".entry-header .entry-title").text

    assert successful_login_heading == successful_login_heading_text




