from idna.idnadata import scripts
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC #for waits
from selenium.webdriver.support.wait import WebDriverWait #For Explicit Waits
import time
import pytest

driver = webdriver.Chrome()

#? Wait Commands
# ? implicit wait  - driver.implicitly_wait()
#           - only need to implement once before driver get.
#         - applicable for all statements after.
#         - general wait before failing/timeout until driver.quit()
#! Disadvantages:
#        - if element is not available within the time period, still can get exception

# ? explicit wait - myVariable = WebDriverWait(driver, timeout=10)
#         - Works based on condition
#         - use variable then class WebDriverWait(driver, seconds)
#! Disadvatages:
#         - Multiple places
#         - More difficult
# ? time.sleep(seconds) - not technically a wait statement -
#       - waits maximum time out
# ! Disadvantages: Poor performance of script
#       - if element is not available within the time period, still can get exception

#? Implicit Wait
# driver.implicitly_wait(5)
driver.get('https://duckduckgo.com')
driver.maximize_window()

#? Implicit Wait

# search_field = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")
# search_field.send_keys('Selenium')
# search_field.send_keys(Keys.ENTER)
#
# sel_link = driver.find_element(By.XPATH,"//p[text()='Selenium']")
# sel_link.click()



#? Explicit Wait
myWait = WebDriverWait(driver, timeout=5)
search_field = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")
myWait.until(lambda _ : search_field.is_displayed()) #waits until true, mind the SPACE
search_field.send_keys('Selenium')
time.sleep(1)
search_field.send_keys(Keys.ENTER)

sel_link = driver.find_element(By.XPATH,"//p[text()='Selenium']")
myWait.until(lambda _ : sel_link.is_displayed()) #waits until true, mind the SPACE


sel_link.click()  #until the presence of element, then click on element
driver.quit()
