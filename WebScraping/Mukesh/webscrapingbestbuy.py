from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import openpyxl



driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bestbuy.com")
driver.implicitly_wait(20)

search_input = driver.find_element(By.ID, "gh-search-input")
search_input.send_keys("Samsung phones")
search_input.send_keys(Keys.ENTER)
samsung_checkbox = driver.find_element(By.ID, "brand_facet-Samsung-0")
samsung_checkbox.click()

my_phone=[]
my_price=[]

# phone_names = driver.find_elements(By.XPATH, "//div[@class=\"column-middle\"]/h4[@class=\"sku-title\"]")
# # first_18_phone_names = phone_names[:18]
# phone_prices = driver.find_elements(By.XPATH, "//div[@class='column-right']//div[@data-testid='customer-price']//span[@aria-hidden='true']")
# # first_18_phone_prices = phone_prices[:18]



phone_names = driver.find_elements(By.XPATH, "//div[@class=\"column-middle\"]/h4[@class=\"sku-title\"]")
for phone in phone_names:
    my_phone.append(phone.text)

print("*" *50)
phone_prices = driver.find_elements(By.XPATH, "//div[@class='column-right']//div[@data-testid='customer-price']//span[@aria-hidden='true']")

for price in phone_prices:
    my_price.append(price.text)


final_list = list(zip(my_phone,my_price))

for data in final_list:
    print(data)

print("Part 1: Write to excel file")


#create new Excel sheet

wb=Workbook()
wb['Sheet'].title='BestBuy Samsung Data'
sh1=wb.active

sh1.append(['Name', 'Price'])

for x in final_list:
    print("Writing to doc")
    sh1.append(x)

wb.save("Final_Samsung_Deals.xlsx")

print("Part 2: Send Email")





driver.quit()

