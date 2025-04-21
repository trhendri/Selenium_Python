from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest



# - Go to home page
# - Add item to cart
# - Go to cart
# - Apply free coupon code (if using demostore.supersqa.com then SSQA100 is a free coupon)
# - Verify total price is 0
# - Click on checkout
# - Fill in the information and place order
# - Verify order confirmation page loads

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://demostore.supersqa.com/")

    yield driver
    driver.quit()

def  test_verify_checkout_works(driver):
    homepage_add_to_cart_buttons = driver.find_elements(By.XPATH, "//a[contains(@href, 'add-to-cart')]")
    homepage_add_to_cart_buttons[0].click()
    cart_button = driver.find_element(By.XPATH, "//a[@title='View cart']")
    cart_button.click()
    coupon_code_field = driver.find_element(By.ID, "coupon_code")
    coupon_code_field.clear()
    coupon_code_field.send_keys("SSQA100")
    apply_coupon_button = driver.find_element(By.XPATH, "//button[@name='apply_coupon']")
    apply_coupon_button.click()

    total_price_text = driver.find_element(By.XPATH, "//tr[@class='order-total']//bdi").text
    assert total_price_text == "$15.00"

    checkout_button = driver.find_element(By.CLASS_NAME, "checkout-button")
    checkout_button.click()
    first_name = "TestName"
    last_name = "TestLastName"
    street_address = "123 Test Address"
    city = "TestCity"
    zipcode = "90210"
    phone = "123 456 8748"
    email = "testtest@gmail.com"

    billing_first_name = driver.find_element(By.ID, "billing_first_name")
    billing_last_name = driver.find_element(By.ID, "billing_last_name")
    billing_street_address = driver.find_element(By.XPATH,"//input[@id='billing_address_1']")
    billing_city = driver.find_element(By.ID, "billing_city")
    billing_zipcode = driver.find_element(By.ID, "billing_postcode")
    billing_phone = driver.find_element(By.ID, "billing_phone")
    billing_email = driver.find_element(By.ID, "billing_email")

    billing_first_name.send_keys(first_name)
    billing_last_name.send_keys(last_name)
    billing_street_address.send_keys(street_address)
    billing_city.send_keys(city)
    billing_zipcode.send_keys(zipcode)
    billing_phone.send_keys(phone)
    billing_email.send_keys(email)


    place_order_button = driver.find_element(By.ID, "place_order")
    place_order_button.click()

    time.sleep(2)
    order_received_confirm = driver.find_element(By.CSS_SELECTOR, ".entry-header .entry-title")
    order_confirm_url = driver.current_url


    assert "order-received" in order_confirm_url
    assert order_received_confirm.text == "Order received"

