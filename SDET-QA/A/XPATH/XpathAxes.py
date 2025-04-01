from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()
driver.get('http://www.money.rediff.com/gainers/bse/daily/groupa')
driver.maximize_window()

#? XPath Axes to travel dom
# self -//a[contains(text(),\'Source Natural Foods\')]/self::a
# parent - Traverse parent element of the current html tag - //*[id="Dude"]/parent::tagname
# child - Traverse all child elements of the current html tag //*[id="Dude"]/child::tagname
# ancestor - Traverse all the ancester elements(grandparent, parent, etc) of the current html tag - //*[id="Dude"]/ancestor::tagname
# descendant  - Traverse all descendent element(child node, grandchild node etc) of the current HTML tag - //*[id="Dude"]/descendant::tagname
# following -  Traverse all elements that come after the current tag - //*[id="Dude"]/following::tagname
# following-sibling - Traverse from current HTML to Next sibling HTML tag - //current html tag[id="Dude"]//following-sibling::sibling tag[@id='dudette']
# preceding - Traverse all nodes that comes before the current html tag - //*[id='dude']/preceding::tagname
# preceding-sibling - Traverse from current html tag to previous sibling html tag -//current html tag[@id='dude']/preceding-sibling::previous tag[@id='dudette']

#?self = Source Natural Foods


self_text = driver.find_element(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/self::a').text #establish self node use as initial reference before using Axes
print(self_text)

parent_text = driver.find_element(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/parent::td').text
print(parent_text)

ancestor_child = driver.find_elements(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr/child::td') #from self, go to ancestor the children
print(len(ancestor_child))

ancestor_text=driver.find_element(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr').text #prints entire row bc ancestor holds all data
print(ancestor_text)

ancestor_descendant = driver.find_elements(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr/descendant::*') #traverse to ancestor to descent and * grabs all tag or if tag is unknown use *
print(len(ancestor_descendant))

ancestor_following = driver.find_elements(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr/following::*')
print(f'Total Following Nodes: {len(ancestor_following)}')

ancestor_following_sibling = driver.find_elements(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr/following-sibling::tr')
print('Number:', len(ancestor_following_sibling))

ancestor_preceding =  driver.find_elements(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr/preceding::tr')
print(f'Preceding Length: {len(ancestor_preceding)}')

ancestor_preceding_sibling =  driver.find_elements(By.XPATH,'//a[contains(text(),\'Source Natural Foods\')]/ancestor::tr/preceding-sibling::tr')
print(len(ancestor_preceding_sibling))

#TODO: Rereview DOM Structure






driver.quit()

