'''
Assignment 3: CSS Selector Challenge -> Locate web elements using CSS Selectors, including selectors with wildcards for elements having varying or dynamic attribute values.Example: Use a CSS wildcard selector to locate elements whose ID starts with user.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)

    username_field = driver.find_element(By.CSS_SELECTOR, "input[name^='user']")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.CSS_SELECTOR, "input[id*='pass']")
    password_field.send_keys("SuperSecretPassword!")

    time.sleep(5)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[class^='radius']")
    submit_button.click()
    time.sleep(7)

    flash_banner = driver.find_element(By.CSS_SELECTOR, "div[class$='success']")
    print(f"Status Message: {flash_banner.text.strip()}")

finally:
    driver.quit()
