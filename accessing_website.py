# This program attempts to download a csv from a selected website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Change to the appropriate WebDriver for your browser

try:
    # Open the webpage
    driver.get("https://help.sap.com/whats-new/6a6876bb02204429bfc72cf8b861a866?locale=en-US")

    # Find the button element by its XPath of the download csv 
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/nav/div[1]/div[1]/div[1]/button/span[2]")))
    
    # Click on the button
    driver.execute_script("arguments[0].click();", element)
    
    # For new users, the subscribe tab will come up, cancel that first
    element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/nav/div[1]/div[1]/div[3]/div[1]/div/header/button")))  # Replace with your full XPath

    # Click the element
    driver.execute_script("arguments[0].click();", element2)
    
    # Find the button element by its XPath of the download csv again
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/nav/div[1]/div[1]/div[1]/button/span[2]")))
    
    # Click on the button
    driver.execute_script("arguments[0].click();", element)
    
    # Click on the one for downloading as semi-colon, can be changed based off button[#]
    element3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/nav/div[1]/div[1]/div[1]/div/div/div/ul/li/button[1]")))  # Replace with your full XPath

    # Click the element
    driver.execute_script("arguments[0].click();", element3)

    # Makes sure for the website to open for 10 seconds to download the file successfully
    time.sleep(10)
    
    #failed test case
    #driver.execute_script('document.evaluate("//button[contains(text(), \'Download CSV\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
    

finally:
    pass