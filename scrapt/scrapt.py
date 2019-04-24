from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import requests
from selenium.webdriver.chrome.options import Options
from models import models


def scrapt_selenium(url):
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(20)
    driver.get(url)
    bs = BeautifulSoup(driver.page_source, 'lxml')
    return bs


def scrap_requets(url):
    data = requests.get(url).text
    return BeautifulSoup(data, 'lxml')
