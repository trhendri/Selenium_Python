from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC #for waits
from selenium.webdriver.support.wait import WebDriverWait #For Explicit Waits
import time
import pytest


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demo.nopcommerce.com')
#alt driver.find_element(By.LINK_TEXT, 'Digital downloads').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Digital').click()


#? Links
# 1. internal links - same page
# 2. external links - other page
# 3. broken links

#find number of links
links = driver.find_elements(By.TAG_NAME, 'a')
#alt links = driver.find_elements(By.XPATH, '//a')
print('Total num of links:', len(links)) #97

#print all link names
for link in links:
    print(link.text)

driver.quit()

#? Broken Links

