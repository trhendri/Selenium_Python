from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses

driver = webdriver.Chrome()
#Test - Verify PyPI Link Works
    #Verify link works
driver.get('https://python.org')
driver.implicitly_wait(10)

current_title = driver.title
expected_title = "Welcome to Python.org"
if current_title != expected_title:
    raise Exception(f"Went to python.org but got wrong title. Current Title: {current_title}") #add error message




search_field_id = '#id-search-field'
search_field_element = driver.find_element(By.CSS_SELECTOR, search_field_id)
search_field_element.send_keys('testing')
go_button_id = 'submit'
go_button_element = driver.find_element(By.ID, go_button_id)
go_button_element.click()

first_result_xpath = '//div[@id="content"]//li[1]'
first_result_element = driver.find_element(By.XPATH, first_result_xpath)
#import pdb; pdb.set_trace() 
#use to see available actions: dir(first_result_element)
#then type c to continue
assert first_result_element.is_displayed(), f"After searching, the result is not displayed"
driver.quit()


