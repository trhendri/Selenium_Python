import pytest
import sys

#? Parameterize to run multiple times with different data

@pytest.mark.parametrize("username, password", [("Selenium", "Webdriver"),("Python","Pytest"),("Jimi","Hendrix")])
def test_login(username, password):
    print(username)
    print(password)