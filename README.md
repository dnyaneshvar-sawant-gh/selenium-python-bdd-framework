# SauceDemo BDD Automation Framework

This repository contains an end-to-end automation framework for testing the [SauceDemo](https://www.saucedemo.com/) web application. It is built using:

- 🐍 Python
- 🌐 Selenium WebDriver
- 🧪 PyTest
- 🥒 Behave (Cucumber BDD)
- 📸 Allure for reporting
- 📁 Page Object Model for code modularity
---

## 📁 Project Structure

SeleniumPythonFramework/
│
├── features/                  # Contains all BDD feature files and step definitions
│   ├── steps/                 # Step definition files
│   ├── environment.py         # Behave hooks (before/after scenarios, etc.)
│   └── *.feature              # Gherkin feature files
│
├── pageObjects/              # Page Object classes for each web page
│   └── *.py                  # e.g., LoginPage.py, AddToCart.py
│
├── utilities/                # Utility classes (e.g., logger, base, config reader)
│   └── *.py
│
├── screenshots/              # Captures screenshots for failed steps
│
├── config.ini                # Configuration file (browser, base URL, etc.)
├── requirements.txt          # Python dependencies
├── scripts.bat               # Batch script to run tagged test scenarios with reporting
└── README.md                 # You're here :)
```

---

## ⚙️ Requirements

- Python 3.9+
- Google Chrome
- pip (Python package manager)
- Allure CLI (for report generation)

---

## 📦 Python Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```text
selenium==4.3.4
behave
allure-behave
configparser
```

---

## 🧪 Run Test Scenarios

### ▶️ Run All Tests

```bash
behave --no-capture -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### ▶️ Run Tests with Specific Tag

```bash
behave -t @tagname --no-capture -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

> Tags like `@Login`, `@AddToCart`, `@RemoveProduct` are defined in feature files.

---

## 📊 Generate Allure Report

```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

---

## 💻 Run with Batch File

To simplify test execution, a `run_behave.bat` script is provided.

```bash
run_behave.bat
```

You can configure:
- `TAG=@tagName`
- `BROWSER_NAME=chrome`
- `CLEAR_REPORT=yes`
- `CLEAR_SCREENSHOT=yes`

---

## 🛠️ Configuration

The `config.ini` file contains all environment-specific settings.

```ini
[default]
base_url = https://www.saucedemo.com/
browser = chrome
```

---

## 📷 Screenshots on Failure

Screenshots are automatically captured for failed steps:
- Attached to Allure report
- Saved in the `screenshots/` folder (if enabled via `.bat` script)

---

## 📋 Sample Feature: Add to Cart

```gherkin
Scenario: Add a multiple item to the cart
    Given User Enter "standard_user" and "secret_sauce" and clicks on login
    When User adds the following items to the cart:
        | Product Name              |
        | Sauce Labs Backpack       |
        | Sauce Labs Bike Light     |
    Then Validate Cart icon should show "2" item
    And Validate "Remove" button should be visible for "Sauce Labs Bike Light"
```

---

## ✅ Best Practices Followed

- Modular Page Object Model (POM)
- Centralized configuration
- Tagged and grouped scenarios
- Screenshot + reporting integration
- Environment hooks via `environment.py`

---

## 🤝 Contributing

Pull requests and improvements are welcome. Please ensure you add relevant test cases or documentation.

---

## 📧 Contact

For any queries, contact: **dnyaneshvarsawant1@gmail.com**
