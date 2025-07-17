from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    cart= (By.XPATH,"//a[@class='shopping_cart_link']")
    remove_button = By.ID, "remove-button"

    def get_cart_item_count(self):
        try:
            cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return cart_badge.text
        except:
            return "0"

    def click_add_to_cart(self, product_name):
        xpath = f"//div[@class='inventory_item']//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(text(),'Add to cart')]"
        add_to_cart = self.driver.find_element(By.XPATH, xpath)
        add_to_cart.click()

    def click_remove(self, product_name):
        xpath = f"//div[@class='cart_item']//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button[text()='Remove']"
        remove_button = self.driver.find_element(By.XPATH, xpath)
        remove_button.click()

    def check_remove_button(self, product_name):
        xpath = f"//div[@class='cart_item']//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button[text()='Remove']"
        remove_button = self.driver.find_element(By.XPATH, xpath)
        return remove_button.text

    def click_cart_option(self):
        self.driver.find_element(*self.cart).click()

