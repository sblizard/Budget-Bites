from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Set variables
page_num: int = 1
location_url: str = 'https://shop.foodlion.com/shop/categories?tags=loyalty_deal'

# Get the page
driver.get(location_url)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-1eer7o2"))
    )
    items = driver.find_elements(By.CLASS_NAME, "css-f85de")
    for item in items:
        print(item.get_attribute("outerHTML"))
finally:
    driver.quit()