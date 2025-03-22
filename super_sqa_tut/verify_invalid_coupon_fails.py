from selenium import webdriver  #import webdriver
from selenium.webdriver.common.by import By  #import By class
from selenium.webdriver.common.keys import Keys #Import Key presses
from selenium.common.exceptions import NoSuchElementException #Import NoSuchElement
import time #to use time.sleep(seconds)

#in devtools:
#$$('.add_to_cart) css
#$x(//a[@type='....']) xpath

#Functions
def open_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #waiting for elements to appear for 10
    return driver

def go_to_home_page(driver): #adding driver so we can call methods on it in future, to interact with elements
    driver.get('http://demostore.supersqa.com')

def add_first_item_to_cart(driver):

    first_add_button = driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
    first_add_button.click()

def go_to_cart_page(driver):
    driver.get('http://demostore.supersqa.com/cart')

def apply_coupon(driver, coupon_code):
    coupon_field = driver.find_element(By.CSS_SELECTOR, '#coupon_code')
    coupon_field.send_keys(coupon_code)
    apply_button = driver.find_element(By.CSS_SELECTOR, '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
    apply_button.click()

def verify_cart_has_item(driver):
    for i in range(5):
        try:
            driver.find_element(By.CLASS_NAME, 'cart_item') #setting loop 5 times to find element
            return #exit out of loop if found
        except NoSuchElementException:
            print("Item not in cart. Retrying after 2 seconds") #print status message
            time.sleep(2) #pause for 2 seconds
            driver.refresh() #reload/refresh page #This will happen 5 times if needed

def get_displayed_error_message(driver):
   return  driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li').text
    




#Function Calls
if __name__ == '__main__':
    driver = open_browser()
    go_to_home_page(driver)
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    verify_cart_has_item(driver)
    apply_coupon(driver,'fakeone')
    get_displayed_error_message(driver)
    error_message = get_displayed_error_message(driver)
    expected_message = 'Coupon "fakeone" does not exist!'
    assert error_message == expected_message, f"Unexpected error message: {error_message}"
    print('PASS')

    
