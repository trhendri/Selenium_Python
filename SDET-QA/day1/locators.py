from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')
driver.find_element(By.CLASS_NAME, 'search-box-button').click()

driver.find_element(By.LINK_TEXT, "Register").click()


driver.quit() #closes all
#driver.close() close on browser at time

# #finding total number of links on webpage:
# you can use links=driver.find_elements(By.TAG_NAME, 'a')
# print(len(links))




