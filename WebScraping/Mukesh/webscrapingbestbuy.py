from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import inspect


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bestbuy.com")
driver.implicitly_wait(10)

search_input = driver.find_element(By.ID, "gh-search-input")
search_input.send_keys("Samsung phones")
search_input.send_keys(Keys.ENTER)
samsung_checkbox = driver.find_element(By.ID, "brand_facet-Samsung-0")
samsung_checkbox.click()

phone_names = driver.find_elements(By.CLASS_NAME, "sku-title")
phone_prices = driver.find_elements(By.XPATH, "//div[@data-testid=\"customer-price\"]//span[@aria-hidden=\"true\"]")
first_18_phone_prices = phone_prices[:18]

my_phone=[]
my_price=[]

for phone in phone_names:
    print(phone.text)
    my_phone.append(phone.text)

print("*" *50)

for price in first_18_phone_prices:
    print(price.text)
    my_price.append(price.text)


final_list = zip(my_phone,my_price)

for data in list(final_list):
    print(data)






driver.quit()

