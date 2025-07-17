import configparser
import os

class ReadConfig:
    def __init__(self, config_path='config/config.ini'):  # ✅ Pointing to subfolder
        self.config = configparser.ConfigParser()
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', config_path))
        print(f"[INFO] Loading config from: {abs_path}")  # Optional for debug
        self.config.read(abs_path)

    def get_app_url(self):
        return self.config.get('app', 'url')

    def get_browser_name(self):
        return self.config.get('settings', 'browser')

    def should_clear_report(self):
        # Priority: Environment variable from .bat > config.ini fallback
        return os.getenv("CLEAR_REPORT", self.config.get('settings', 'clear_report', fallback="no")).lower() == 'yes'