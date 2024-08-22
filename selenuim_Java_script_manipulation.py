#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:28:12 2024

@author: ahmeds
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Specify the path to the ChromeDriver
chrome_driver_path = '/home/ahmeds/Downloads/chromedriver-linux64/chromedriver'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome browser with the Service object
driver = webdriver.Chrome(service=service)


# Open a website to verify it works
driver.get("https://www.google.com")

# Find the search box
box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]') 
 
# Enter text in the search area
box.send_keys('web scraping')

# Press Enter to intiate the search
box.send_keys(Keys.ENTER)

# Click on google search to intiate the search
button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
button.click()

# Clicking on a search result
link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[9]/div/div/div[1]/div/div/span/a/h3')
link.click()

# Taking a screenshot
driver.save_screenshot('/home/ahmeds/Downloads/screenshot.png')



# Open a website to verify it works
driver.get("https://www.google.com")

# Find the search box
box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]') 
 
# Enter text in the search area
box.send_keys('lion')

# Press Enter to intiate the search
box.send_keys(Keys.ENTER)

# Select image
driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()

# Take a screenshot of an image
driver.find_element(By.XPATH, '//*[@id="dimg_24"]').screenshot('/home/ahmeds/Downloads/screenshot2.png')

# Self scrolling
driver.execute_script('return document.body.scrollHeight')

driver.execute_script('window.scrollTo(0,20000)')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
# Wait time
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lfootercc')))
