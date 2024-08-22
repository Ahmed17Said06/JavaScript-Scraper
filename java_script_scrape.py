#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:03:38 2024

@author: ahmeds
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Specify the path to the ChromeDriver
chrome_driver_path = '/home/ahmeds/Downloads/chromedriver-linux64/chromedriver'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome browser with the Service object
driver = webdriver.Chrome(service=service)

# Open a website to verify it works
driver.get("https://www.goat.com/sneakers/")

'//*[@id="grid-body"]/div/div[1]/div[1]/a/div[1]/div[2]/div/div[1]/span'

# Find element by using xpath
driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div[1]/a/div[1]/div[2]/div/div[1]/span').text

# Printing value of element using xpath
for i in range(1,30):
    price = driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div[1]/span').text
    print(price)
    
# Open a website to verify it works
driver.get("https://www.google.com")

box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]') 
 
box.send_keys('web scraping')

box.send_keys(Keys.ENTER)

    
    
    




# Close the browser
#driver.quit()




