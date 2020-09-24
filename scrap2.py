from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep
from random import randint
sns.set()

headers = ({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'})

sapo = "https://www.realo.be/en/search/for-sale/province-brussels-capital-region"
response = get(sapo, headers=headers)
# print(response)
# print()

html_soup = BeautifulSoup(response.text, 'html.parser')
price_containers = html_soup.find_all('div', class_="label-price")

prices = []
for i in price_containers:
    prices.append(i.text)
print(prices)

house_containers = html_soup.find_all('li', class_="component-estate-list-grid-item")
first = house_containers[0]
#

house_price = (first.find('div', class_="label-price")).text
house_type = (first.find('span', class_="type")).text.strip()
temp = first.find('div', class_="address")
house_address = (temp.find('a')).text
temp = first.find('div', class_="details")
temp = temp.find_all('span')
temp2 = []
details = {'date_posted': "", 'beds': "", 'bath': "", 'area': ""}
for i in temp:
    temp2.append(i.text)

details['date_posted'] = temp2[0] + ' Ago'
details['beds'] = temp2[1]
details['bath'] = temp2[2]
details['area'] = temp2[3]

print(house_type)
print(house_address)
print(house_price)
print(details)

