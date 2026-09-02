'''
Assignment 2: Multiple Element Identification -> Identify multiple elements of the same type on a webpage and use Selenium to find and work with the list of elements.Example: Find all links on a webpage and print their text
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://testautomationpractice.blogspot.com/")

    links = driver.find_elements(By.TAG_NAME, "a")

    print(f"Total Web Elements found: {len(links)}\n" + "-" * 40)

    for index, link in enumerate(links, start=1):
        link_text = link.text.strip()    

        if link_text:
            print(f"[{index}] Text: {link_text}")

finally:
    driver.quit()
