from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses
from selenium.common.exceptions import NoSuchElementException #Import NoSuchElement
import time #to use time.sleep(seconds)


from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

#Always write test steps before test code.
# WebDriver Instances
    # Every test case should have its own WebdRiver instance
    # Test case independence
    # Always quit the Webdriver(not close)
    # Otherwise, drivers and browsers can become zombie processes! - clean up




#Gherkin - BDD - Given When Then And
# Scenario: Basic DuckDuckGo Search
#Using Page Objects
def test_basic_duckduckgo_search(browser): #'browser'from conftest.py

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = 'panda'

    # Given the DuckDuckGo home page is displayed
    search_page.load()
   
    # When the user searches for "panda"
    search_page.search(PHRASE)

    # Then the search result title contains "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result query is "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    # And the search result links to "panda"
    raise Exception('Incomplete Test') #to signal test isnt ready

#Page object - an object representing a web page or component
# -has locators for finding elements on the page 
# -has interaction methods that interact with the page under test
# Each web page or component under test should have a page object class
# Page Object methods first and then selenium webdriver calls later

#pages under test
#? -DDG Search Page    - DDG Result Page 
# 1. Load thepage        1. Get the result link titles
# 2. search a phrase     2. Get the search input value 
#                        3. Get the title
#? Frequent calls
# For Webdriver:
# current.url
# find_element
# find_elements
# find_element_by*
# get
# maximize_window
# quit
# refresh
# save_screenshot
# title

# For Elements:
# clear
# click
# find_element*
# get_attribute
# get_property
# is_displayed
# location
# send_keys
# size
# text