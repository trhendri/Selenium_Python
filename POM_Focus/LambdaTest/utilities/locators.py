from selenium.webdriver.common.by import By

class ChangePasswordLocatorFields:
    password_field = (By.ID, "input-password")
    confirm_password = (By.ID, "input-confirm")
    continue_button = (By.XPATH, "//input[value='Continue']")
    confirmation_error_message = (By.XPATH, "//div[@class='text-danger']")

