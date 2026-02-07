from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))

try:
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"))
    wait = WebDriverWait(driver, 10)
    award_img = wait.until(
        EC.presence_of_element_located(("id", "award"))
    )

    wait.until(
        lambda d: award_img.get_attribute("src")
    )

    src_value = award_img.get_attribute("src")
    print(src_value)

finally:
    driver.quit()
