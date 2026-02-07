import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Открыть страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Устанавливаем задержку
    delay_input = driver.find_element("id", "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Выполняем операцию
    driver.find_element("xpath", "//span[text()='7']").click()
    driver.find_element("xpath", "//span[text()='+']").click()
    driver.find_element("xpath", "//span[text()='8']").click()
    driver.find_element("xpath", "//span[text()='=']").click()

    # Ждем результат (до 50 секунд)
    wait = WebDriverWait(driver, 50)

    # Ждем, пока результат появится на экране
    screen = driver.find_element("class name", "screen")

    # Используем ожидание с кастомным условием
    wait.until(
        lambda d: screen.text == "15"
    )

    # Проверяем результат
    result = screen.text
    assert result == "15", f"Expected '15', but got '{result}'"

    print(f"✓ Result after 45 seconds: {result}")
    print("✓ Test completed successfully!")
