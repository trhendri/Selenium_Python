from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):#! a 'constructor' thats called each time when you create an object for classm argument 'driver'
        self.driver = driver

        #? Add Objects
        self.profile_picture_xpath = '//img[@alt="profile picture"]'
        self.logout_button_xpath = '//a[@role ="menuitem" and contains(text(), "Logout")]'



    def click_profile_picture(self):
        self.driver.find_element(By.XPATH, self.profile_picture_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath)

