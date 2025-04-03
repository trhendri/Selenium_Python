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

driver.get('https://the-internet.herokuapp.com/javascript_alerts')


#! JS Alert Popup
alert_button = driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]')
alert_button.click()
time.sleep(2)
wait = WebDriverWait(driver, timeout = 2)
alert = wait.until(lambda d : d.switch_to.alert)

alert_text= alert.text
alert.accept()
print(alert_text)


#! JS Confirm Popup
confirm_button = driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]')
confirm_button.click()
time.sleep(2)
wait = WebDriverWait(driver, timeout = 2)
confirm = wait.until(lambda d : d.switch_to.alert)

confirm_text = confirm.text
confirm.dismiss()
print(confirm_text)


#!JS Prompt Popup
prompt_button = driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]')
prompt_button.click()
time.sleep(2)

wait = WebDriverWait(driver, timeout = 2)
prompt = wait.until(lambda d : d.switch_to.alert)

prompt_text = prompt.text
prompt.send_keys("Selenium")
time.sleep(2)
print(prompt_text)
prompt.accept()










driver.quit()

