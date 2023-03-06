import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
option.add_argument('--incognito')
option.add_argument('--headless')
driver = webdriver.Chrome()

URL="https://elmir.ua/"

driver.get(URL)
page_source = driver.page_source
soup = BeautifulSoup(page_source,'html.parser')
print(soup.prettify())

