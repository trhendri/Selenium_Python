from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses

driver = webdriver.Chrome()
#Test - Verify PyPI Link Works
    #Verify link works

driver.get('https://python.org')
current_title = driver.title
expected_title = "Welcome to Python.org"
if current_title != expected_title:
    raise Exception(f"Went to python.org but got wrong title. Current Title: {current_title}") #add error message

pypi_header_link_locator = "a[title='Python Package Index']"
pypi_header_link_element = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator )
pypi_header_link_element.click()

current_url = driver.current_url #get current url
expected_url = 'https://pypi.org/'

assert current_url == expected_url, f"Clicked on PyPi but the url opened was {current_url}" #assertion, error message
print('PASS')
