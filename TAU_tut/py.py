from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses
from selenium.common.exceptions import NoSuchElementException #Import NoSuchElement
import time #to use time.sleep(seconds)

#Always write test steps before test code.
#Gherkin - BDD
# Scenario: Basic DuckDuckGo Search
    # Given the DuckDuckGo home page is displayed
    # When the user searches for "panda"
    # Then the search result title contains "panda"
    # And the search result query is "panda"
    # And the search result links to "panda"

