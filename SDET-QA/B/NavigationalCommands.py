from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()

#? 2. Navigational Commands/Methods
# back()
# forward()
# refresh()


driver.get('https://snapdeal.com')
driver.get('https://amazon.com')

driver.maximize_window()

driver.back() #- goes back to the original window snapdeal.com
time.sleep(5)
driver.forward() # - goes forward to the amazon.com

driver.refresh() #-refresh page
time.sleep(2)

driver.quit()