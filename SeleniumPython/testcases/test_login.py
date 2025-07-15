import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readConfig import ReadConfig

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())

    login_page = LoginPage(driver)
    login_page.setUserName(ReadConfig.getUsername())
    login_page.setPassword(ReadConfig.getPassword())
    time.sleep(3)
    login_page.clickLogin()

    assert "dashboard" in driver.current_url.lower()
