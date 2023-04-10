from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

driverpath='..\\build\\connect\\localpycs\\ms\\driver.exe'
os.environ['PATH'] += os.pathsep + driverpath
driver = webdriver.Edge(driverpath) 
driver.get("http://www.facebook.com")
username = driver.find_element(By.ID,'username') 
password = driver.find_element(By.ID,'password')
username.send_keys("username")  
password.send_keys("password") 
password.send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()
