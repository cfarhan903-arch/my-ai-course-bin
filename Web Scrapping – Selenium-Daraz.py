from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
cService = webdriver.ChromeService(executable_path='C:\\Users\\Admin\\Downloads\\chromedriver-win64\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
driver.get(url)
print("Scrolling to load products...")
for i in range(5):
    driver.execute_script("window.scrollBy(0, 800);")

productsdiv = driver.find_elements(By.CLASS_NAME, "Bm3ON")
products=[]

print(f"Found {len(productsdiv)} products. Extracting URLs...")

for product in productsdiv:
    name = product.find_element(By.TAG_NAME, "a")
    url =  name.get_attribute('href')
    url = url.split("?")[0] if url else "N/A"
    print(url)
    p_price = product.find_element(By.CLASS_NAME, "ooOxS").text
    p_price = p_price.split()[1] if p_price else "N/A"
    print(p_price)
    '''original_price = product.find_elements(By.CLASS_NAME, "ooOxS")
    original_price = not discount = product.find_elements(By.CLASS_NAME, "ooOxS")
    original_price = original_price.split()[1] if original_price else "N/A"'''  
    p_name = product.find_element(By.CLASS_NAME, "RfADt").text
    p_name = p_name.split()[0] if p_name else "N/A"
    print(p_name)
    units_sold = product.find_element(By.CLASS_NAME, "_6uN7R").text
    units_sold = units_sold.split()[0] if units_sold else "N/A"
    print(units_sold)
    
    products.append({'Product Name': p_name, 'Price': p_price, 'Product URL': url, 'Units Sold': units_sold})

with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Product Name', 'Price', 'Product URL', 'Units Sold'])
    writer.writeheader()
    writer.writerows(products)  
print("Data saved to products.csv")
driver.quit()