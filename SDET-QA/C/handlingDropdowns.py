from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC #for waits
from selenium.webdriver.support.wait import WebDriverWait #For Explicit Waits
import time
import pytest
from selenium.webdriver.support.select import Select #import Select Class


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://qa-practice.netlify.app/dropdowns')
dropdown_country_element = driver.find_element(By.XPATH, '//select[@id="dropdown-menu"]')
dropdown_country = Select(dropdown_country_element)

#Select option from the dropdown
# dropdown_country.select_by_visible_text('Japan')
# dropdown_country.select_by_value('Benin')
dropdown_country.select_by_index(2)
time.sleep(3)

#capture all options and print them
all_countries = driver.find_elements(By.TAG_NAME, 'option')


#alt for country in all_countries:
#alt  country_name = country.text
#alt     print(country_name)

country_options = dropdown_country.options

for country in country_options:
    print(country.text)



print("Total Number of Options: ", len(dropdown_country.options)) #print options

#select option from dropdown without using built in method

for country in country_options:
    if country.text == "Zambia":
        country.click()
        break














driver.quit()