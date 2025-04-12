import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()
driver.implicitly_wait(10)
phone_menu_button = driver.find_element(By.LINK_TEXT, 'Phones & PDAs')
phone_menu_button.click()
iphone_button = driver.find_element(By.LINK_TEXT, 'iPhone')
iphone_button.click()
iphone_gallery = driver.find_element(By.XPATH, '//img[@title="iPhone"]')
iphone_gallery.click()
forward_button = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')
# forward_button.click()
# forward_button.click()
# forward_button.click()
# forward_button.click()
# forward_button.click()

for i in range(0,5):
    forward_button.click()
    time.sleep(2)


#? Create Screenshot - driver.save_screenshot('filename'+ NUMBER-string-random integer num from 1-100 + 'filetype')
driver.save_screenshot('screenshot#'+ str(random.randint(0,101)) + '.png')

exit_gallery = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
exit_gallery.click()

quantity_box = driver.find_element(By.ID, 'input-quantity')
quantity_box.click()
quantity_box.clear()
quantity_box.send_keys('2')

# add_to_cart_button = driver.find_element(By.XPATH,'//div[@id="product"]//button[@type="button"]')
# add_to_cart_button.click()

laptops_menu_dropdown = driver.find_element(By.LINK_TEXT, 'Laptops & Notebooks')

#? TO HOVER
action = ActionChains(driver)
action.move_to_element(laptops_menu_dropdown).perform()

laptops_submenu = driver.find_element(By.LINK_TEXT, 'Show AllLaptops & Notebooks')
laptops_submenu.click()

HP_model = 'HP LP3065'

select_laptop = driver.find_element(By.XPATH, '//a[contains(text(),"HP LP3065")]')
select_laptop.click()

laptop_add_to_cart = driver.find_element(By.XPATH, '//div[@id="product"]//button[@id="button-cart"]')
action = ActionChains(driver)
action.scroll_to_element(laptop_add_to_cart)

# laptop_add_to_cart.location_once_scrolled_into_view

# #Directly add Date in Calendar
# date_input = driver.find_element(By.ID, 'input-option225')
# date_input.clear()
# date_input.send_keys('2026-12-31')

#Traverse the Calendar
calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar.click()

month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')
next_button = driver.find_element(By.XPATH, '//th[@class="next"]')

while month_year.text != 'December 2026':
    next_button.click()

day = driver.find_element(By.XPATH, '//td[text()="31"]')
day.click()

laptop_add_to_cart.click()

cart_total = driver.find_element(By.XPATH, '//span[@id="cart-total"]')
cart_total.click()

checkout_button = driver.find_element(By.XPATH, '//strong[normalize-space()="Checkout"]')
checkout_button.click()
time.sleep(3)


guest_checkout = driver.find_element(By.XPATH, '//label[normalize-space()="Guest Checkout"]')
guest_checkout.click()

checkout_continue_button = driver.find_element(By.XPATH, '//input[@id="button-account"]')
checkout_continue_button.click()
time.sleep(2)

#Billing Details

#firstname
first_name = driver.find_element(By.ID,'input-payment-firstname')
first_name.click()
first_name.send_keys('Jimi')

#lastname
last_name = driver.find_element(By.ID,'input-payment-lastname')
last_name.click()
last_name.send_keys('Hendrix')

#email
email = driver.find_element(By.ID,'input-payment-email')
email.click()
email.send_keys('jimmmyhen@gmail.com')

#telephone
telephone = driver.find_element(By.ID,'input-payment-telephone')
telephone.click()
telephone.send_keys('8085554343')

#address
address_1 =  driver.find_element(By.ID,'input-payment-address-1')
address_1.click()
address_1.send_keys('555 Address Road')

#city
city = driver.find_element(By.ID,'input-payment-city')
city.click()
city.send_keys('Chicago')

#postcode
post_code = driver.find_element(By.ID,'input-payment-postcode')
post_code.click()
post_code.send_keys('50468')

#country
country = driver.find_element(By.ID,'input-payment-country')
dropdown_1 = Select(country)
dropdown_1.select_by_value('71')
time.sleep(2)


#region
region = driver.find_element(By.ID,'input-payment-zone')
dropdown_2 = Select(region)
dropdown_2.select_by_visible_text('Rotuma')

billing_continue_button = driver.find_element(By.ID, 'button-guest')
billing_continue_button.click()

delivery_continue_button = driver.find_element(By.ID, "button-shipping-method")
delivery_continue_button.click()
time.sleep(2)

#accept terms and conditions
tc_checkbox = driver.find_element(By.XPATH, '//input[@name="agree"]')
tc_checkbox.click()

payment_continue_button = driver.find_element(By.ID, 'button-payment-method')
payment_continue_button.click()
time.sleep(2)

#final price
total_order_amount = driver.find_element(By.XPATH,'//body[1]/header[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/div[1]/table[1]/tbody[1]/tr[4]/td[2]').text
print(f'The final price of products is: {total_order_amount}')
time.sleep(2)

confirm_order_button = driver.find_element(By.ID, 'button-confirm')
confirm_order_button.click()
time.sleep(2)

confirmation_message = driver.find_element(By.XPATH, '//div[@id="content"]/h1').text
time.sleep(2)

print(f'The confirmation message is: {confirmation_message}')







































driver.quit()