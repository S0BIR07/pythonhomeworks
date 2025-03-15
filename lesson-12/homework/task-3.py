from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json, requests
import time   # need to put some sleep time between operations to load pages and prevent errors

# Initial URL
base_url = "https://www.demoblaze.com/"
# Handle webdriver exception and other exceptions
try:
    chrome_options = webdriver.ChromeOptions()  
    driver = webdriver.Chrome(options=chrome_options)  
    driver.get(base_url)
except WebDriverException as e:
    print(f"WebDriver Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(2)
#Go to the laptops section
laptops_button = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_button.click()
time.sleep(2)
#Click the next button
next_button = driver.find_element(By.ID, "next2")
next_button.click()
time.sleep(2)
#Get list of links for laptops
laptops = driver.find_elements(By.CLASS_NAME, "hrefch")
#Get details of each laptop by iterating through laptops
laptop_data = []
for laptop in laptops:
    laptop.click()
    time.sleep(2)
    laptop_data.append({"name":driver.find_element(By.CLASS_NAME, "name").text, "price": driver.find_element(By.CLASS_NAME, "price-container").text, "description": driver.find_element(By.ID, "more-information").text})
    driver.back()
    time.sleep(2)
#Save exctracted information in a structured JSON format
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptop_data, f, indent=4)
driver.quit()