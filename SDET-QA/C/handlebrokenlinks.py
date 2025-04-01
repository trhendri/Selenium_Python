from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC #for waits
from selenium.webdriver.support.wait import WebDriverWait #For Explicit Waits
import time
import pytest
import requests as requests #to use requests package

#? Broken Links
# install requests package through file-->Settings-->ProjectInterpretor --> + ..> Requests
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, 'a')

print(len(all_links))

count = 0
for link in all_links:
    url=link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print(url, 'is broken link')
        count+=1
    else:
        print(url," is valid links")

print("Total number of broken links: ", count)




driver.quit()