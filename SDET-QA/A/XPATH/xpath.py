from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

#XPATH
# Absolute / Full Xpath - /html/body/nav/div/div/div[2]/ul/li[2]/a
# Relative / Partial Xpath - //*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a




driver = webdriver.Chrome()

# def func(x):
#     return x+1
# def test_answer():
#     assert func(3) ==5

# XPATH options:
# and - //input[@name='name' and @placeholder='Full Name']
# or - //input[@name='organization_name' or @placeholder='Organization']
# contains() - //input[contains(@id,'st')]
# starts-with() -//input[starts-with(@id,'st')]
# text() - //input[text()='Women']
#TODO: Review additonal xpath :https://devhints.io/xpath

#? XPath Axes to travel dom
# self
# parent - Traverse parent element of the current html tag - //*[id="Dude"]/parent::tagname
# child - Traverse all child elements of the current html tag //*[id="Dude"]/child::tagname
# ancestor - Traverse all the ancester elements(grandparent, parent, etc) of the current html tag - //*[id="Dude"]/ancestor::tagname
# descendant  - Traverse all descendent element(child node, grandchild node etc) of the current HTML tag - //*[id="Dude"]/descendant::tagname
# following -  Traverse all elements that come after the current tag - //*[id="Dude"]/following::tagname
# following-sibling - Traverse from current HTML to Next sibling HTML tag - //current html tag[id="Dude"]//following-sibling::sibling tag[@id='dudette']
# preceding - Traverse all nodes that comes before the current html tag - //*[id='dude']/preceding::tagname
# preceding-sibling - Traverse from current html tag to previous sibling html tag -//current html tag[@id='dude']/preceding-sibling::previous tag[@id='dudette']


