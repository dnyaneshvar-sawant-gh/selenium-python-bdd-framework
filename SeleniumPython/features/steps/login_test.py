import os
import time

from behave import *

from pageObjects.LoginPage import LoginPage
from utils.browser_utils import BrowserUtils
from utilities.common_utils import CommonUtils

use_step_matcher("re")


@given('User Enter "(?P<username>.+)" and "(?P<password>.+)" and clicks on login')
def step_impl(context, username, password):
    login_page = LoginPage(context.driver)
    username = username.strip()
    password = password.strip()
    if username == '""' and password != '""':
        login_page.enter_password(password)
        login_page.click_login()
    elif password == '""' and username != '""':
        login_page.enter_username(username)
        login_page.click_login()
        time.sleep(1)
    elif username == '""' and password == '""':
        login_page.click_login()
    else:
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        time.sleep(1)


@step("Validate Successful login")
def step_impl(context):
    current_url = context.driver.current_url
    assert "inventory" in current_url, f"Login failed. Current URL: {current_url}"


@then("User Logout from the Application")
def step_impl(context):
    login_page = LoginPage(context.driver)
    time.sleep(1)
    CommonUtils.accept_alert_if_present(context.driver)
    login_page.click_menu()
    time.sleep(1)
    login_page.click_logout()
    time.sleep(1)
    assert "saucedemo.com" in context.driver.current_url


@given("User launches the browser and opens the application")
def step_impl(context):
    browser_name = os.getenv("BROWSER_NAME", "chrome")
    url = context.test_config.get_app_url()

    browser_utils = BrowserUtils()
    context.driver = browser_utils.launch_browser(browser_name)
    browser_utils.open_url(context.driver, url)

    # Save for reuse
    context.browser_utils = browser_utils


@step('Validate Error Message as "(?P<expected_error>.+)"')
def step_impl(context, expected_error):
    login_page = LoginPage(context.driver)
    time.sleep(1)
    error_message = login_page.get_error_message()
    time.sleep(1)
    assert error_message == expected_error
