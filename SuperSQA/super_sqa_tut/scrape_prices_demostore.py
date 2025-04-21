from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses
from selenium.common.exceptions import NoSuchElementException #Import NoSuchElement
import time #to use time.sleep(seconds)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
url = 'http://demostore.supersqa.com'
driver.get(url)

all_products = driver.find_elements(By.CLASS_NAME, 'product-type-simple')
print(f'Number of Products: {len(all_products)}') #grabs number of products

all_product_and_price = []
for product in all_products:
    price_element = product.find_element(By.CSS_SELECTOR, 'span.amount')
    price = price_element.text
    name_element = product.find_element(By.CSS_SELECTOR,'h2.woocommerce-loop-product__title')
    name = name_element.text
    print(price)
    print(name)
    
    all_product_and_price.append({'name': name, 'price': price}) #dictionary
print(len(all_product_and_price))
print(all_product_and_price)
