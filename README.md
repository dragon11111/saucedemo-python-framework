# SauceDemo E2E Automation Framework (Python/Pytest)

![Allure Report](allure_dashboard.png)

## 📌 Overview
This is a professional-grade End-to-End (E2E) UI automation framework built to test the SauceDemo e-commerce platform. It demonstrates a modern, data-driven architecture using **Python**, **Pytest**, and **Selenium WebDriver**. 

Originally architected in Java/TestNG, this framework was successfully migrated to Python to leverage highly readable syntax, dynamic tuple-based locators, and Pytest's powerful fixture management.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Test Runner:** Pytest
* **Browser Automation:** Selenium WebDriver (Chrome)
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Allure Reports

## 🏗️ Architecture & Features
* **`conftest.py` Fixtures:** Completely replaces traditional setup/teardown methods. Injects a clean, incognito headless browser session into every test automatically.
* **Smart Explicit Waits:** The `BasePage` utilizes Selenium's `WebDriverWait` to dynamically wait for elements to be clickable or visible, completely eliminating flaky `time.sleep()` calls.
* **Dynamic Locators:** The `InventoryPage` generates locators on the fly based on product names, adhering to DRY (Don't Repeat Yourself) principles.
* **Dependency Management:** Managed cleanly via `requirements.txt`.

## 🚀 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/dragon11111/saucedemo-python-framework.git](https://github.com/dragon11111/saucedemo-python-framework.git)
   cd saucedemo-python-framework