from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
links = driver.find_elements(By.TAG_NAME, 'a')


print(len(sliders))
print(len(links))

driver.quit()

