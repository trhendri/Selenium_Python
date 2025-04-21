from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses
import pdb #python debugger
#from selenium.webdriver.ui import WebDriverWait # Explicit Wait
    #ie. elm=webDriverWait(driver, 10).until (....)
    #more recommended
#from selenium.webdriver.support import expected_conditions as EC





#Finding Elements
# find_element(By..., <locator>)
# find_elements(By..., <locator)
## By.ID             ## By.LINK_TEXT
## By.CSS_SELECTOR   ## By.PARTIAL_LINK_TEXT
## By.XPATH          ## By.NAME
## By.CLASS_NAME     ## By.TAG_NAME
#CSS most commonly used

#DEPRECATED FYI
## find_element_by_id(<locator>)    ## find_element_by_css_selector(<locator)
## find_element_by_xpath(<locator) ## etc etc etc

#create an instance "driver" is general variable"
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com')
print(driver.title)

#driver.quit() #quit all browsers
#driver.close() #close the current browser

# By.ID
cart = driver.find_element(By.ID, 'site-header-cart')
print(cart)
print(type(cart))
cart_txt = cart.text #gets test of the element
print(cart_txt)

search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoodie') #add text to input field
search_field.send_keys(Keys.ENTER)

#By.LINK_TEXT
my_account = driver.find_element(By.LINK_TEXT,'My account')
my_account.click()

#pdb.set_trace() #Test breaks/stop at this point instead of continuous run

## WebDriver Waits
#implicit wait

driver.implicitly_wait(10) #wait 10 seconds until returning cant find element etc

#explicit wait

