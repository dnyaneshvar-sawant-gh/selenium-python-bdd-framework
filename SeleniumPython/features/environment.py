import os
import shutil

import allure

from utilities.readConfig import ReadConfig
from utils.browser_utils import BrowserUtils
from allure_commons.types import AttachmentType
from datetime import datetime


def before_all(context):
    config = ReadConfig()
    context.test_config = config

    # Prepare base report path
    base_reports_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'reports'))
    allure_results_path = os.path.join(base_reports_path, 'allure-results')

    if config.should_clear_report():
        if os.path.exists(base_reports_path):
            print("Clearing existing reports...")
            shutil.rmtree(base_reports_path)
        os.makedirs(allure_results_path)
    else:
        # Make sure folders exist even if not clearing
        if not os.path.exists(base_reports_path):
            os.makedirs(base_reports_path)
        if not os.path.exists(allure_results_path):
            os.makedirs(allure_results_path)

    print(f"[INFO] Allure results will be saved to: {allure_results_path}")


def before_scenario(context, scenario):
    try:
        config = ReadConfig()
        browser = os.getenv("BROWSER_NAME", config.get_browser_name())

        utils = BrowserUtils()
        context.driver = utils.launch_browser(browser)

        # Save for use in background or steps
        context.browser_utils = utils
        context.config = config
    except Exception as e:
        print(f"[ERROR in before_scenario]: {e}")
        context.driver = None  # Ensure this exists for after_scenario


def after_step(context, step):
    if step.status == "failed":
        try:
            # Get the first tag from the scenario (customize if needed)
            tag_name = context.scenario.tags[0] if context.scenario.tags else "no_tag"

            # Create Screenshots directory if it doesn't exist
            screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Generate filename using tag name and timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{tag_name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)

            # Save screenshot to file
            context.driver.save_screenshot(filepath)
            print(f"[INFO] Screenshot saved to {filepath}")

            # Attach to Allure
            with open(filepath, "rb") as image_file:
                allure.attach(image_file.read(), name="screenshot_on_failure", attachment_type=AttachmentType.PNG)
            print("[INFO] Screenshot attached to Allure report.")

        except Exception as e:
            print(f"[ERROR] Failed to capture or save screenshot: {e}")


def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
