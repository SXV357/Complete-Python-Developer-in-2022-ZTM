from random import choice
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/Automation/chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
chrome_browser = webdriver.Chrome(service = service, options = options)

chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.title
for text in ['Enter message', 'Show Message']:
    assert text in chrome_browser.page_source # for generally checking if anything exists in page's content

message_field = chrome_browser.find_element(By.CLASS_NAME, 'form-control')
message_field.clear()
text_messages = ["Hello World", "Hi there!", "What's good", "Hell no!"]
message_field.send_keys(choice(text_messages)) # populates that input field with what is passed into send_keys()

time.sleep(3)

button_elem = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
button_elem.click()

text_display = chrome_browser.find_element(By.ID, 'display')
print(text_display.get_attribute('innerHTML')) # will get what is between the opening anc closing tags of that element

time.sleep(10)
chrome_browser.quit()