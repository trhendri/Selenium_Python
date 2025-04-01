from errno import ECHILD

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome()

driver.get('http://www.automationpractice.pl/index.php?')
driver.maximize_window()

#Aboslute xpath
# driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/input[4]').send_keys('T-shirts')
# driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/button').click()



driver.find_element(By.XPATH, '//*[@id="search_query_top"]').send_keys('T-shirts')
driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').send_keys('T-shirts')




