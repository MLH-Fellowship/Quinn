from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import re 

brands = []
brands_list = []

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.sephora.com/brands-list"

page = driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

main = soup.find('main', attrs={'class' : 'css-1vs8v5v'})
results = main.find_all('a', attrs={'class':'css-ekc7zl'})

for brand in results:
    b = brand.getText()
    brands.append(b)

for b in brands:
    clean_b = re.sub(r'[^a-zA-Z ]', '', b)
    brands_list.append(clean_b)

my_file = open('brands.txt', 'w')
my_file.write('Brands')
my_file.write('\n')
for ele in brands_list:
    my_file.write(ele)
    my_file.write('\n')
my_file.close()

if __name__ == '__main__':
    print(brands_list)