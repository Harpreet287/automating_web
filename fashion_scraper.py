import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://wgsn.com/en/blogs")

link_element = (WebDriverWait(driver, 12)
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.item-thumb a"))))
link_element.click()


wait = WebDriverWait(driver, 10)
wait.until(EC
           .presence_of_all_elements_located((By.CSS_SELECTOR, "div.field--label-hidden.field--items")))

divs = driver.find_elements(By.CSS_SELECTOR, "div.field--label-hidden.field--items")


for div in divs:
    paragraphs = div.find_elements(By.TAG_NAME, "p")

    for paragraph in paragraphs:

        if paragraph.get_attribute("class") == "strong":
            print(paragraph.text)
        else:
            print(paragraph.text)
driver.quit()
