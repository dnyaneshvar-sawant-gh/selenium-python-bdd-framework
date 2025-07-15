from selenium.webdriver.common.by import By

class LoginPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    txt_username = (By.NAME, "username")
    txt_password = (By.NAME, "password")
    btn_login = (By.XPATH, "//button[@type='submit']")

    # Actions
    def setUserName(self, username):
        self.driver.find_element(*self.txt_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*self.txt_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.btn_login).click()
