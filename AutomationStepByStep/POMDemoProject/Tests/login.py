
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

#?Troubleshoot commandline to run test but just nav through parent folders
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from AutomationStepByStep.POMDemoProject.Pages.loginPage import LoginPage
from AutomationStepByStep.POMDemoProject.Pages.homePage import HomePage

import HtmlTestRunner

class LoginTest(unittest.TestCase): #! Define class and name it, (logintest) then in parens, unittest.TestCase to pull from builtin unittest functions

    @classmethod #! add before class methods
    def setUpClass(cls): #! Runs once before all test methods
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):

        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password('admin123')
        login.click_login()


        homepage = HomePage(driver)
        homepage.click_profile_picture()
        homepage.click_logout()

        time.sleep(3)
        driver.quit()

    def test_02_login_invalid_username(self):

        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password('admin123')
        login.click_login()
        message = driver.find_element(By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
        self.assertEqual(message, "Invalid credentials123")
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print('Test Completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/spasi/Projects/Selenium_Python/AutomationStepByStep/POMDemoProject/Reports"))



