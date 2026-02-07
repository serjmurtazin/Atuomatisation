import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_saucedemo_total_price(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

    add_buttons = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for button_id in add_buttons:
        driver.find_element("id", button_id).click()

    driver.find_element("class name", "shopping_cart_link").click()

    driver.find_element("id", "checkout").click()

    driver.find_element("id", "first-name").send_keys("Иван")
    driver.find_element("id", "last-name").send_keys("Петров")
    driver.find_element("id", "postal-code").send_keys("660022")

    driver.find_element("id", "continue").click()

    wait.until(EC.presence_of_element_located(
        ("class name", "summary_total_label")))

    total_element = driver.find_element("class name", "summary_total_label")
    total_text = total_element.text  # "Total: $58.29"

    total_value = total_text.replace("Total: $", "")

    assert total_value == "58.29", f"Expected $58.29, but got ${total_value}"
