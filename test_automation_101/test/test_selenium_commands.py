from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def firefox():
    #initialize firefox driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_button(firefox):
    firefox.get('https://admlucid.com/Home/WebElements')
    firefox.implicitly_wait(10)
    title = firefox.title
    assert title == '- Admlucid'

    Button4 = firefox.find_element(By.ID, 'Button4')
    Button4.click()
    firefox.switch_to.alert.accept()

def test_clickButtonAfterValidateText(firefox):
    firefox.get('https://admlucid.com/Home/WebElements')
    Button1 = firefox.find_element(By.ID, 'Button1')

    if 'button 1' in Button1.get_attribute(name='value'):
        print(Button1.isEnabled())
        Button1.click()
        print(Button1.is_displayed())
    






