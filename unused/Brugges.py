from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep
from random import randint
sns.set()

headers = (
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'})

sapo = "https://www.realo.be/en/search/for-sale/brugge"
response = get(sapo, headers=headers)
# print(response)
# print()

html_soup = BeautifulSoup(response.text, 'html.parser')

# price_containers = html_soup.find_all('div', class_="label-price")
# prices = []
# for i in price_containers:
#     prices.append(i.text)
# print(prices)
# type_containers = html_soup.find_all('span', class_="type")
# types = []
# for i in type_containers:
#     types.append(i.text)
# print(types)


house_containers = html_soup.find_all(
    'li', class_="component-estate-list-grid-item")
first = house_containers[0]

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

# print(house_type)
# print(house_address)
# print(house_price)
# print(details)
df = pd.DataFrame(
        columns=['House_Type', 'House_Price', 'House_Address', 'House_Details'])

for first in house_containers:
    house_price = (first.find('div', class_="label-price")).text
    print(house_price)
    house_type = (first.find('span', class_="type")).text.strip()
    print(house_type)
    temp = first.find('div', class_="address")
    house_address = (temp.find('a')).text
    print(house_address)
    temp = first.find('div', class_="details")
    temp = temp.find_all('span')
    details = []
    # details = {'date_posted': "", 'beds': "", 'bath': "", 'area': ""}
    for i in temp:
        details.append(i.text)
    print(details)
    print()

    df = df.append({'House_Type': house_type, 'House_Price': house_price,
                    'House_Address': house_address, 'House_Details': details}, ignore_index=True)


print(df)
df.to_csv('Brugges.csv')
