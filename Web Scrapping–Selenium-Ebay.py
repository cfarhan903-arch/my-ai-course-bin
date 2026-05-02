'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
cService = webdriver.ChromeService(executable_path='C:\\Users\\Admin\\Downloads\\chromedriver-win64\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
driver.get(url)

print("Scrolling to load products...")
for i in range(5):
    driver.execute_script("window.scrollBy(0, 800);")

productsdiv = driver.find_elements(By.XPATH, "//div[@class='brwrvr__item-card']")
products = []
print(f"Found {len(productsdiv)} products. Extracting URLs...")
for product in productsdiv:
    name = product.find_element(By.CLASS_NAME,"brwrvr__item-card")
    url = name.find_element(By.TAG_NAME, "a").get_attribute("href") if name else "N/A"
    print(url)
products.append({ 'Product URL': url})'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

# Chrome Driver
cService = webdriver.ChromeService(
    executable_path=r'C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
)

driver = webdriver.Chrome(service=cService)

driver.get(url)

driver.maximize_window()

# Wait for page load
time.sleep(5)

print("Scrolling to load products...")

# Scroll slowly
for i in range(5):
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(2)

# Better selector
productsdiv = driver.find_elements(
    By.XPATH,
    "//*[contains(@class,'brwrvr__item-card')]"
)

print(f"Found {len(productsdiv)} products")

products = []

for product in productsdiv:

    try:
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = "N/A"

    print(link)

    products.append({
        "Product URL": link
    })

driver.quit()