from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest





# #n Go to My account page directly
# Generate a random email address and password
# Fill in the registration form verify user gets logged in by verifying the logged in my accont page loads
#
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://demostore.supersqa.com/my-account/")

    yield driver
    driver.quit()

def test_new_user_registration(driver):

    register_email_field = driver.find_element(By.ID, "reg_email")
    register_password_field = driver.find_element(By.ID, "reg_password")
    register_button = driver.find_element(By.XPATH, "//button[@name='register']")

    register_email_field.click()
    register_email_field.clear()
    register_email_field.send_keys("testemrtrtrail@gmail.com")
    register_password_field.click()
    register_password_field.clear()
    register_password_field.send_keys("testpassword123")
    register_button.click()
    my_account_url = driver.current_url

    assert driver.current_url == my_account_url








