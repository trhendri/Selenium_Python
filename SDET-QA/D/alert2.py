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
driver.implicitly_wait(2)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')



signin_button = driver.find_element(By.XPATH,'//button[@class="signin-btn"]')
signin_button.click()
time.sleep(2)
wait = WebDriverWait(driver, timeout = 2)
alert = wait.until(lambda d : d.switch_to.alert)

alert_text= alert.text
alert.accept()
print(alert_text)

driver.quit()