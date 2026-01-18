from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.CSS_SELECTOR, ".example input[type='number']")
input_field.send_keys("Sky")
sleep(1)
input_field.clear()
sleep(1)
input_field.send_keys("Pro")
sleep(1)
driver.quit()
