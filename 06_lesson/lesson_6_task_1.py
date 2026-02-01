from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))

try:
    driver.get("http://uitestingplayground.com/ajax")
    ajax_button = driver.find_element("id", "ajaxButton")
    ajax_button.click()
    wait = WebDriverWait(driver, 20)
    success_element = wait.until(
        EC.text_to_be_present_in_element(
            ("css selector", "p.bg-success"),
            "Data loaded"
        )
    )

    element = driver.find_element("css selector", "p.bg-success")
    print(element.text)

finally:
    driver.quit()
