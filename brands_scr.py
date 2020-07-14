from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

brands = []
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.sephora.com/brands-list"

page = driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

if __name__ == '__main__':
    print(soup)