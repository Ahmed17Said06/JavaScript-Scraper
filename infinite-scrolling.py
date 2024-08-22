#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:07:09 2024

@author: ahmeds
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time


# Specify the path to the ChromeDriver
chrome_driver_path = '/home/ahmeds/Downloads/chromedriver-linux64/chromedriver'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome browser with the Service object
driver = webdriver.Chrome(service=service)


# Open a website to verify it works
driver.get("https://www.nike.com/w/sale-3yaep")

time.sleep(3)

# get rid of the cookies pop-up
cookies_pop_up = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/div/section/div[2]/div/button')
if (cookies_pop_up):    
    driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/div/section/div[2]/div/button').click()

time.sleep(2)

# get rid of the area pop-up
driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div/div/div/section/div[1]/div[1]/button').click()

# Self scrolling
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        print('breaked the while loop')
        break
    last_height = new_height
    
    
soup = BeautifulSoup(driver.page_source, 'lxml')

product_card =  soup.find_all('div', class_ = 'product-card__body')
len(product_card)

data = []

#df = pd.DataFrame({'link':[''], 'Name':[''], 'Subtitle':[''], 'Price':[''], 'Sale price': ['']})

for product in product_card:
    try:
        link = product.find('a', class_ = 'product-card__link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text.strip()
        subtitle = product.find('div', class_ = 'product-card__subtitle').text.strip()
        price = product.find('div', class_ = 'product-price us__styling is--striked-out css-0').text.strip()
        sale_price = product.find('div', class_ = 'product-price is--current-price css-1ydfahe').text.strip()
        data.append({'link': link, 'Name': name, 'Subtitle': subtitle, 'Price': price, 'Sale price': sale_price})
    except:
        pass

df = pd.DataFrame(data)

print(df)

df.to_csv('./nike.csv')
    





