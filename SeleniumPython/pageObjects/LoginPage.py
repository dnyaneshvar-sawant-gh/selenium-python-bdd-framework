from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")
    error_message = (By.XPATH, "//div[@class='error-message-container error']")

    # Actions
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
