from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    wait = WebDriverWait(driver, 10)
    flash_element = wait.until(EC.presence_of_element_located((By.ID, "flash")))

    message = flash_element.text.split('\n')[0]
    print(f"Сообщение: {message}")

finally:
    driver.quit()
