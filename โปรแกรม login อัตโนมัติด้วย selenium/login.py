from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
username = "Username"
password = "123456"

# เปิด Browser
driver = webdriver.Chrome()

# เปิด web page
driver.get('https://www.facebook.com')

user = driver.find_element(By.XPATH, '//*[@id="email"]')
pas = driver.find_element(By.XPATH, '//*[@id="pass"]')
time.sleep(2)
user.send_keys(username)
time.sleep(3)
pas.send_keys(password + Keys.ENTER)

while True:
    time.sleep(1)