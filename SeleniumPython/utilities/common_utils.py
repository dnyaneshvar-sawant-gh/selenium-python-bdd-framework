from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

class CommonUtils:
    def open_application(self, driver, config):
        url = config.get_app_url()
        print(f"Opening URL: {url}")
        driver.get(url)

    def accept_alert_if_present(driver):
        try:
            alert = Alert(driver)
            alert_text = alert.text
            print(f"[INFO] Alert found with message: {alert_text}")
            alert.accept()
            print("[INFO] Alert accepted.")
        except NoAlertPresentException:
            print("[INFO] No alert present.")
