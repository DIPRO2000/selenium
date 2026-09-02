import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Target JSFiddle which opens its editor canvas instantly without login redirects
driver.get("https://jsfiddle.net")

# adding a small delay to let the panels load fully on the screen
time.sleep(10)

# Switch to iframe (important)
# switching to jsfiddle live result frame to find elements inside it
driver.switch_to.frame("result")

# Locate button inside body (child selector)
# using child operator > to target the direct body child element for assignment 4
button = driver.find_element(By.CSS_SELECTOR, "body > p")

print("Element found successfully inside the iframe!")

input("Press Enter to close...")

driver.quit()
