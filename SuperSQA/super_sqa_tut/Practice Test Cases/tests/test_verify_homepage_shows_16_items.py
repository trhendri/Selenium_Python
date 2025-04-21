from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://demostore.supersqa.com/my-account/")

    yield driver
    driver.quit()

def test_verify_home_page_shows_16_items(driver):
    driver.get('http://demostore.supersqa.com/')
    homepage_products = driver.find_elements(By.CSS_SELECTOR,"#primary .product")
    total_products = len(homepage_products)

    assert total_products == 16




