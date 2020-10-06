from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep
from random import randint
sns.set()
import re

headers = (
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'})

sapo = "https://www.luxevastgoed.be/en/offer/location=8300-knokke%20heist+selection=for%20sale"


df = pd.DataFrame(columns=['link', 'title', 'img_links', 'price', 'description', 'lot-area', 'liv-area', 'lat-lon', 'Property-id', 'Type of House', 'lot surface area', 'bedrooms', 'garages', 'asking price', 'living area', 'year of const', 'bathrooms', 'shower-rooms' ])

for i in range(1,10):
    response = get(sapo + "+page="+str(i), headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    house_container = html_soup.find_all('div', class_="b-row-products")


    house_container_1 = house_container[0]
    house_container_2 = house_container[1]
    for house in house_container_1:
        link = house.find('a', class_="c-property")
        link = link['href']
        response_2 = get(link, headers)
        html_soup_2 = BeautifulSoup(response_2.text, 'html.parser')
        title = (html_soup_2.find('h1', class_="h2")).text
        img_container = html_soup_2.find('div', class_="swiper-wrapper")
        img_links = []
        temp = img_container.find_all('img')
        for i in temp:  
            try:
                img_links.append(i['src'])
            except:
                img_links.append(i['data-src'])
        
        description = (html_soup_2.find('div', {'id': 'collapse-description-body'})).text
        price = (html_soup_2.find('div',class_="px-2")).text
        area = html_soup_2.find_all('div', class_="p-2")
        lot_area = area[0].text
        lot_area = lot_area[16:]
        liv_area = area[1].text
        liv_area = liv_area[11:]

        temp = html_soup_2.find("div", { "id":"collapse-properties"} )
        table = temp.find_all("tr")

        values = []

        for tr in table:
            values.append((tr.find('td')).text)
            # print(key + ": " + value)
        
        location = html_soup_2.find('div', {'id': 'map'})
        location = location['data-map-options']
        lat = location[8:21]
        lon = location[30:43]
        lat_lon = lat+ "," + lon

        df = df.append({'link': link, 'title': title, 'img_links': img_links, 'price': price, 'description': description, 'lot-area': lot_area, 'liv-area': liv_area, 'lat-lon': lat_lon, 'Property-id': values[0] , 'Type of House': values[2], 'lot surface area': values[4], 'bedrooms': values[6], 'garages': values[8], 'asking price': values[1], 'living area': values[3], 'year of const': values[5], 'bathrooms': values[7], 'shower-rooms': values[9] }, ignore_index=True)

        print()

    for house in house_container_2:
        link = house.find('a', class_="c-property")
        link = link['href']
        response_2 = get(link, headers)
        html_soup_2 = BeautifulSoup(response_2.text, 'html.parser')
        title = (html_soup_2.find('h1', class_="h2")).text
        img_container = html_soup_2.find('div', class_="swiper-wrapper")
        img_links = []
        temp = img_container.find_all('img')
        for i in temp:  
            try:
                img_links.append(i['src'])
            except:
                img_links.append(i['data-src'])
        
        description = (html_soup_2.find('div', {'id': 'collapse-description-body'})).text
        price = (html_soup_2.find('div',class_="px-2")).text
        area = html_soup_2.find_all('div', class_="p-2")
        lot_area = area[0].text
        lot_area = lot_area[16:]
        liv_area = area[1].text
        liv_area = liv_area[11:]

        temp = html_soup_2.find("div", { "id":"collapse-properties"} )
        table = temp.find_all("tr")

        values = []

        for tr in table:
            values.append((tr.find('td')).text)
            # print(key + ": " + value)
        
        location = html_soup_2.find('div', {'id': 'map'})
        location = location['data-map-options']
        lat = location[8:21]
        lon = location[30:43]
        lat_lon = lat+ "," + lon

        df = df.append({'link': link, 'title': title, 'img_links': img_links, 'price': price, 'description': description, 'lot-area': lot_area, 'liv-area': liv_area, 'lat-lon': lat_lon, 'Property-id': values[0] , 'Type of House': values[2], 'lot surface area': values[4], 'bedrooms': values[6], 'garages': values[8], 'asking price': values[1], 'living area': values[3], 'year of const': values[5], 'bathrooms': values[7], 'shower-rooms': values[9] }, ignore_index=True)

        print()
        
    print(df)


df.to_csv('./csvs/Knokke_luxury_properties.csv')