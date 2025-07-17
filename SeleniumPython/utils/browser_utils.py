import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


class BrowserUtils:

    def launch_browser(self, browser_name):
        try:
            browser_name = browser_name.lower()

            if browser_name == 'firefox':
                print("Launching Firefox browser...")
                options = FirefoxOptions()
                options.set_preference("dom.webnotifications.enabled", False)
                options.set_preference("geo.enabled", False)

                driver = webdriver.Firefox(service=FirefoxService(), options=options)
                driver.maximize_window()
                return driver

            elif browser_name == 'edge':
                print("Launching Edge browser...")
                options = EdgeOptions()
                options.add_experimental_option("prefs", {
                    "profile.default_content_setting_values.notifications": 2,
                    "profile.default_content_setting_values.geolocation": 2
                })

                driver = webdriver.Edge(service=EdgeService(), options=options)
                driver.maximize_window()
                return driver

            else:
                print("Launching Chrome browser...")
                chrome_options = Options()

                # Create temporary user profile
                temp_profile = tempfile.mkdtemp()
                chrome_options.add_argument(f"--user-data-dir={temp_profile}")

                # Disable password manager and autofill
                prefs = {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                    "autofill.profile_enabled": False,
                    "autofill.credit_card_enabled": False
                }
                chrome_options.add_experimental_option("prefs", prefs)

                # Suppress other features
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_argument("--disable-infobars")
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument("--incognito")

                driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
                driver.maximize_window()
                return driver
        except Exception as e:
            print(f"[ERROR] Failed to launch browser '{browser_name}': {e}")
            return None  # Always return something, even on failure

    def open_url(self, driver, url):
        try:
            print("Opening URL: " + url)
            driver.get(url)
        except Exception as e:
            print(f"[ERROR] Failed to open URL '{url}': {e}")
