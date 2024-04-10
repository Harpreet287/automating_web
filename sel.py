import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
lang = (WebDriverWait(driver, 10)
        .until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))))
lang.click()
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bigCookie')))

button = driver.find_element(By.ID, 'bigCookie')
productprice_pref = 'productPrice'
product_pref = 'product'


time.sleep(2)
while True:
    button.click()
    cur_cookie_count = driver.find_element(By.ID, 'cookies').text.split(' ')[0]
    cur_cookie_count = int(cur_cookie_count.replace(',',''))
    for i in range(1,4):
        product_price = driver.find_element(By.ID, productprice_pref+str(i)).text.replace(',','')
        if( not product_price.isdigit()):
            continue
        product_price = int(product_price)
        # print(cur_cookie_count,product_price)
        if(cur_cookie_count>=product_price):
            product = driver.find_element(By.ID, product_pref+str(i))
            product.click()
            break





print("BIG")
time.sleep(99)
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME ,'gLYyf')))




# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Instagram")))



time.sleep(200)
driver.quit()


