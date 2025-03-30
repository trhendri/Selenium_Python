from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

#XPATH
# Abolsute / Full Xpath - /html/body/nav/div/div/div[2]/ul/li[2]/a
# Relative / Partial Xpath - //*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a

# XPATH options:
# and
# or
# contains()
# starts-with()
# text()


driver = webdriver.Chrome()
def func(x):
    return x+1
def test_answer():
    assert func(3) ==5