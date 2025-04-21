from selenium import webdriver
from selenium.webdriver.common.by import By



class Locators:

    #Login page objects
    username_textbox_xpath = '//input[@placeholder="Username"]'
    password_textbox_xpath = '//input[@placeholder="Password"]'
    login_button_xpath = '//button[@type="submit"]'

    #Home page objects
    profile_picture_xpath = '//img[@alt="profile picture"]'
    logout_button_xpath = '//a[@role ="menuitem" and contains(text(), "Logout")]'