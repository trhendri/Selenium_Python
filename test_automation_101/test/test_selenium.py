from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest #from conftest file?

def test_1(chrome):
    chrome.get('https://www.admlucid.com')
    title = chrome.title
    assert title == 'Home Page - Admlucid'

def test_2(chrome):
    chrome.get('https://www.admlucid.com')
    url = chrome.current_url
    assert url == 'https://www.admlucid.com/'

    