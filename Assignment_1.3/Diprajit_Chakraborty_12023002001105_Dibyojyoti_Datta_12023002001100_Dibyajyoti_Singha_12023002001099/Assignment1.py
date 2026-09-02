'''
Assignment 1: Locating Web Elements -> Use Selenium to identify web elements
on a webpage using different locator strategies such as ID, NAME, TAG_NAME,
LINK_TEXT, and CLASS_NAME.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# 1. Locate by ID
name = driver.find_element(By.ID, "name")

# 2. Locate by NAME
navbar = driver.find_element(By.NAME, "Navbar")

# 3. Locate by TAG_NAME
input_element = driver.find_element(By.TAG_NAME, "input")

# 4. Locate by LINK_TEXT
link = driver.find_element(By.LINK_TEXT, "Errorcode 408")

# 5. Locate by CLASS_NAME
element = driver.find_element(By.CLASS_NAME, "form-control")

# Print the located element details
print("By ID:", name.get_attribute("id"))
print("By NAME:", navbar.get_attribute("name"))
print("By TAG_NAME:", input_element.tag_name)
print("By LINK_TEXT:", link.text)
print("By CLASS_NAME:", element.get_attribute("class"))

driver.quit()
