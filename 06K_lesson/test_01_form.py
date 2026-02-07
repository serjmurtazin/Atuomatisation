import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    service = EdgeService(r"E:\▲Tools▲\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(5)
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        input_field = driver.find_element(
            "css selector", f"input[name='{field_name}']")
        input_field.send_keys(value)

    submit_button = driver.find_element(
        "css selector", "button[type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 3)

    zip_code_div = driver.find_element("id", "zip-code")

    wait.until(
        lambda d: "alert-danger" in zip_code_div.get_attribute("class")
    )

    zip_code_class = zip_code_div.get_attribute("class")
    assert "alert-danger" in zip_code_class, \
        f"Zip code field should be red, but has classes: {zip_code_class}"
    print("Zip code field is highlighted in red")

    green_fields_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields_ids:
        field = driver.find_element("id", field_id)
        field_class = field.get_attribute("class")

        assert ("alert-success" in field_class), \
            f"Field {field_id} should be green, but has classes: {field_class}"
        print(f"Field '{field_id}' is highlighted in green")

    print(f"\nAll {len(green_fields_ids)} fields are highlighted in green")
    print("All assertions passed successfully!")
