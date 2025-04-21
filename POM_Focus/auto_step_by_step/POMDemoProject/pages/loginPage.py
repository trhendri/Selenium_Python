from selenium.webdriver.common.by import By
from POM_Focus.auto_step_by_step.POMDemoProject.locators.locators import locators


class LoginPage:

    def __init__(self, driver):#! a 'constructor' thats called each time when you create an object for classm argument 'driver'
        self.driver = driver

        #? Add Objects
        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.password_textbox_xpath =  '//input[@placeholder="Password"]'
        self.login_button_xpath= '//button[@type="submit"]'
        self.invalid_username_message_xpath = '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'


    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_username_message(self):
        message = self.driver.find_element(By.XPATH, self.invalid_username_message_xpath).text
        return message

