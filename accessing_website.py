# This program attempts to download a csv from a selected website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Change to the appropriate WebDriver for your browser

try:
    # Open the webpage
    driver.get("https://help.sap.com/whats-new/6a6876bb02204429bfc72cf8b861a866?locale=en-US")

    # Find the button element by its XPath, possible for other buttons but not download csv
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Help')]")))
    
    # Click on the button
    driver.execute_script("arguments[0].click();", element)
    
    #failed test case
    #driver.execute_script('document.evaluate("//button[contains(text(), \'Download CSV\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
    

finally:
    # Close the browser window
    driver.quit()