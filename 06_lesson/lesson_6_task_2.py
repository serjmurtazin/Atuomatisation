from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))

try:
    driver.get("http://uitestingplayground.com/textinput")
    input_field = driver.find_element("id", "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")
    button = driver.find_element("id", "updatingButton")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            ("id", "updatingButton"),
            "SkyPro"
        )
    )

    updated_button = driver.find_element("id", "updatingButton")
    button_text = updated_button.text
    print(button_text)

finally:
    driver.quit()
