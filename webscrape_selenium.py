from selenium import webdriver
from selenium.common import exceptions
import pandas as pd
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.get('http://www.google.com/')
time.sleep(5)
search_box = browser.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) 
browser.quit()
