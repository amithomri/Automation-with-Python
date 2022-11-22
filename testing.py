from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
"""
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

"""

service = Service(".\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert "Selenium Easy Demo" in driver.title
show_message_button = driver.find_element(By.CLASS_NAME, 'btn-default')
assert show_message_button.text in driver.page_source
user_message = driver.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I AM THE BOSS")
show_message_button.click()
output_message = driver.find_element(By.ID, "display")
user_button = driver.find_element(By.CSS_SELECTOR, '.btn')
driver.quit()
