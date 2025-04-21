from POM_Focus.LambdaTest.pages.login_page import LoginPage
from POM_Focus.LambdaTest.tests.base_test import BaseTest
from POM_Focus.LambdaTest.utilities.test_data import TestData
from selenium import webdriver


class TestLogin(BaseTest):
    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        actual_title = login_page.get_title()
        assert actual_title == "My Account"

    def test_invalid_credentials(self):
       login_page = LoginPage(self.driver)
       login_page.log_into_application(
           "Invalid Email", "Invalid Password")
       actual_message = login_page.get_warning_message()
       assert actual_message.__contains__("Warning")