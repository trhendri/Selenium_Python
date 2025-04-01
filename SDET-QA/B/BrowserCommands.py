from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()
driver.maximize_window()

#? 2. Browser Commands
# driver.close() - one window/browser current
# driver.quit() --all browser/windows and kills driver process itself


driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()

driver.implicitly_wait(2)

orange_inc_footer = driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")
orange_inc_footer.click()

time.sleep(5)

driver.close() #Closes first window

time.sleep(5)

driver.quit()