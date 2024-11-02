from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

# Set variables
page_num: int = 1
location_url: str = 'https://shop.foodlion.com/shop/categories?tags=loyalty_deal'

# Get the page
driver.get(location_url)

try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-1eer7o2"))
    )

    # Scroll and load items
    last_height = driver.execute_script("return document.body.scrollHeight")
    i: int = 1
    while i!=11:
        # Scroll down by smaller increments
        driver.execute_script("window.scrollTo(0, "+str(i*1000)+");")
        
        # Wait for new items to load
        time.sleep(3)
        
        # # Calculate new scroll height and compare with last scroll height
        # new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     break
        # last_height = new_height
        i+=1
    
    items = driver.find_elements(By.CLASS_NAME, "css-f85de")
    for item in items:
        print(item.get_attribute("outerHTML"))
finally:
    driver.quit()