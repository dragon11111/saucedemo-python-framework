import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    print("\n[SETUP] Initializing Chrome WebDriver...")

    # 1. Set up our Chrome Options
    chrome_options = Options()
    # This disables the "Save Password" popup
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    # Run in incognito mode for a clean session
    chrome_options.add_argument("--incognito")
    # Hide the "Chrome is being controlled by automated software" banner
    chrome_options.add_argument("--disable-infobars")

    # 2. Pass those options into the driver
    my_driver = webdriver.Chrome(options=chrome_options)
    my_driver.maximize_window()
    my_driver.implicitly_wait(10)

    yield my_driver

    print("\n[TEARDOWN] Closing Chrome WebDriver...")
    my_driver.quit()