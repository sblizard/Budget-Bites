from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from src.database.modle import Ingredient
import requests
import time
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def scrape_page(page_num: int):
    location_url: str = 'https://shop.foodlion.com/shop/categories?tags=loyalty_deal&page='+str(page_num)

    # Get the page
    driver.get(location_url)

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-1eer7o2"))
        )

        # Scroll and load items
        last_height = driver.execute_script("return document.body.scrollHeight")
        i: int = 1
        while i!=7:
            driver.execute_script("window.scrollTo(0, "+str(i*1000)+");")
            time.sleep(1)
            i+=1
        
        item_names = driver.find_elements(By.CLASS_NAME, "css-f85de")
        item_base_prices = driver.find_elements(By.CLASS_NAME, "css-6a7b9b")
        item_loyalty_prices = driver.find_elements(By.CLASS_NAME, "css-1x3un8e")
        for i in range(len(item_names)):
            name_html = item_names[i].get_attribute("outerHTML")
            base_price_html = item_base_prices[i].get_attribute("outerHTML")
            loyalty_price_html = item_loyalty_prices[i].get_attribute("outerHTML")
            
            name_soup = BeautifulSoup(name_html, 'html.parser')
            base_price_soup = BeautifulSoup(base_price_html, 'html.parser')
            loyalty_price_soup = BeautifulSoup(loyalty_price_html, 'html.parser')
            
            name = name_soup.get_text()
            base_price = base_price_soup.get_text()
            loyalty_price = loyalty_price_soup.get_text()

            base_price = float(re.search(r'\d+\.\d+', base_price).group())
            loyalty_price = float(re.search(r'\d+\.\d+', loyalty_price).group())
            discount_amount = base_price - loyalty_price
            
            ingredient = Ingredient(
                ingredient_name=name, 
                ingredient_id="0", 
                base_price=base_price, 
                sale_price=loyalty_price, 
                discount_amount=discount_amount
            )

            response = requests.post(
                'http://localhost:8000/ingredient/create',
                json=ingredient.model_dump_json()
            )

            print(f"Name: {name}, Base Price: {base_price}, Loyalty Price: {loyalty_price}")
    except Exception as e:
        print(f"Error: {e}")


for (page_num) in range(1,99):
    scrape_page(page_num)

driver.quit()