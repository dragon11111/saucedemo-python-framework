from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# --- LOGIN TESTS ---

def test_valid_login(driver):
    print("\n  -> Navigating to SauceDemo...")
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    print("  -> Logging in with valid credentials...")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url, "User was not redirected to inventory page."


def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_message()
    assert "locked out" in error_text, "Locked out error message did not appear."


def test_invalid_password(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.login("standard_user", "wrong_password")

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text, "Invalid credentials error did not appear."


# --- CART & INVENTORY TESTS ---
# We log in at the start of these tests to reach the inventory page

def test_add_single_item_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)

    print("  -> Adding Backpack to cart...")
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    assert inventory_page.get_cart_count() == "1", "Cart badge count is incorrect."


def test_add_multiple_items_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)

    print("  -> Adding Backpack and Bike Light to cart...")
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.add_item_to_cart("sauce-labs-bike-light")

    assert inventory_page.get_cart_count() == "2", "Cart badge did not update to 2."


def test_remove_item_from_cart(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)

    inventory_page.add_item_to_cart("sauce-labs-onesie")
    print("  -> Removing Onesie from cart...")
    inventory_page.remove_item_from_cart("sauce-labs-onesie")

    # We use a try/except because when the cart is empty, the badge disappears from the HTML
    try:
        inventory_page.get_cart_count()
        cart_has_badge = True
    except:
        cart_has_badge = False

    assert cart_has_badge is False, "Cart badge is still visible after removing all items."


def test_add_specific_item_fleece_jacket(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)

    print("  -> Adding Fleece Jacket to cart...")
    inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")

    assert inventory_page.get_cart_count() == "1", "Failed to add Fleece Jacket to cart."


# --- NAVIGATION & SESSION TESTS ---

def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)

    print("  -> Opening hamburger menu and logging out...")
    inventory_page.logout()

    assert "inventory.html" not in driver.current_url, "User was not redirected away from inventory."
    assert driver.find_element(*LoginPage.LOGIN_BUTTON).is_displayed(), "Login button is not visible after logout."


def test_unauthorized_access_redirects_to_login(driver):
    print("  -> Attempting to bypass login directly to inventory...")
    driver.get("https://www.saucedemo.com/inventory.html")

    login_page = LoginPage(driver)
    error_text = login_page.get_error_message()

    assert "You can only access '/inventory.html' when you are logged in" in error_text


def test_performance_glitch_user_login(driver):
    print("  -> Testing login for performance_glitch_user...")
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    # This user takes a few seconds to log in on purpose.
    # Our smart waits handle this automatically without time.sleep()!
    login_page.login("performance_glitch_user", "secret_sauce")

    assert "inventory.html" in driver.current_url, "Performance user failed to reach inventory."