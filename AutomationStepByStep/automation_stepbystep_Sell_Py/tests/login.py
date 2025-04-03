
##? Check libraries
# pip list
# pip freeze
# pip show selenium   -> view libraries
# pip check selenium -> check for broken requirements

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time #can use to pause browser
import unittest #imports in-built unit test model
import pytest

#TODO: 2. Implement Unit Testing
class LoginTest(unittest.TestCase): #create class to call unit test
    @classmethod
    def setUpClass(cls): #to run only once before all test methods/mind variable and use before running method
    #setUp(self) - runs before every test method 
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element(By.NAME, "username").send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)
        
    @classmethod
    def tearDown(cls): #tearDownClass(cls) runs after every test
        #tearDown(self) - runs once after all tests completed 
        return super().tearDown()
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")






