from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

# - Go to home page
# - Item to cart
# - Go to cart
# - Click the 'x' icon to remove item from cart
# - Verify success message
# - Verify cart is empty

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://demostore.supersqa.com/")

    yield
    driver.quit()

def test_verify_removing_item_from_cart(driver):


    pass