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

sapo = "https://www.realo.be/en/search/for-sale/knokke-heist"

df = pd.DataFrame(columns=['link', 'Title/Address', 'img_links', 'price', 'description', 'bedrooms', 'bathrooms', 'habital_area', 'EPC certificate number', 'property_type', 'score'])
main_link = "https://www.realo.be"


# response = get(sapo, headers = headers)
# html_soup = BeautifulSoup(response.text, 'html.parser')
# print(response)

# house_container = html_soup.find_all('li', class_="component-estate-list-grid-item")
# for house in house_container:
#     sublink = house.find('a', class_="link")
#     sublink = sublink['href']
#     response_1 = get(main_link+ sublink, headers=headers)
#     html_soup2 = BeautifulSoup(response_1.text, 'html.parser')

#     img_links = html_soup2.find('div', class_="gallery")
#     img_links = (img_links.find('img'))['src']

#     title = (html_soup2.find('h1', class_="address")).text.strip()
#     try:
#         price = (html_soup2.find('span', class_="price")).text
#     except:
#         price = "-"

#     try:
#         description = html_soup2.find('div', class_="component-property-description")
#         description = (description.find('div')).text
#     except:
#         price = "-"
#         description = "-"


#     details = {}
#     table = html_soup2.find('div', 'component-property-features')
#     table = table.find('tbody')
    
#     table = table.find_all('tr')
#     # print(table)
#     for row in table:
#         name = (row.find('td', class_="name")).text.strip()
#         value = (row.find('td', class_="value")).text.strip()
#         details[name] = value
    

#     try:
#         bedrooms = details['Bedrooms']
#     except:
#         bedrooms = "-"
#     try:
#         bathrooms = details['Bathrooms']
#     except:
#         bathrooms = "-"
#     try:
#         habital_area = details['Habitable area']
#     except:
#         habital_area = "-"
#     try:
#         certicate_number = details['EPC certificate number']
#     except:
#         certicate_number = "-"
#     try:
#         property_type = details['Property type']
#     except:
#         property_type = "-"

#     # print(bedrooms, bathrooms, habital_area, certicate_number, property_type)

#     try:
#         score = (html_soup2.find("div", class_="percent-ball")).text
#     except:
#         score ="-"
#     # print(main_link+ sublink, response_1)
#     # print(len(img_links))
#     # print(title)
#     # print(price)
#     # print(description)
#     # print(len(table))
#     # print(score)
#     # print("####################################################")
#     df = df.append({'link': main_link+sublink, 'Title/Address': title, 'img_links': img_links, 'price': price, 'description': description, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'habital_area': habital_area, 'EPC certificate number': certicate_number, 'property_type': property_type, 'score': score}, ignore_index=True)

for j in range(1,12):
    if j> 1:
        sapo = sapo + "?page=" + str(j)
    response = get(sapo + "?page=" + str(j), headers = headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
   
    house_container = html_soup.find_all('li', class_="component-estate-list-grid-item")
    for house in house_container:
        sublink = house.find('a', class_="link")
        sublink = sublink['href']
        response_1 = get(main_link+ sublink, headers=headers)
        print(main_link+ sublink, response_1, j)
        html_soup2 = BeautifulSoup(response_1.text, 'html.parser')

        img_links = html_soup2.find('div', class_="gallery")
        img_links = (img_links.find('img'))['src']

        title = (html_soup2.find('h1', class_="address")).text.strip()
        try:
            price = (html_soup2.find('span', class_="price")).text
        except:
            price = "-"

        try:
            description = html_soup2.find('div', class_="component-property-description")
            description = (description.find('div')).text
        except:
            price = "-"
            description = "-"


        details = {}
        try:
            table = html_soup2.find('div', 'component-property-features')
            table = table.find('table')
            table = table.find('tbody')
        
            table = table.find_all('tr')
            # print(table)
            for row in table:
                name = (row.find('td', class_="name")).text.strip()
                value = (row.find('td', class_="value")).text.strip()
                details[name] = value
            

            try:
                bedrooms = details['Bedrooms']
            except:
                bedrooms = "-"
            try:
                bathrooms = details['Bathrooms']
            except:
                bathrooms = "-"
            try:
                habital_area = details['Habitable area']
            except:
                habital_area = "-"
            try:
                certicate_number = details['EPC certificate number']
            except:
                certicate_number = "-"
            try:
                property_type = details['Property type']
            except:
                property_type = "-"
        except:
            bedrooms = "-"
            bathrooms = "-"
            habital_area = "-"
            certicate_number = "-"
            property_type = "-"

        try:
            score = (html_soup2.find("div", class_="percent-ball")).text
        except:
            score ="-"
        print(bedrooms, bathrooms, habital_area, certicate_number, property_type)
        print()
        # print(len(img_links))
        # print(title)
        # print(price)
        # print(description)
        # print(len(table))
        # print(score)
        # print("####################################################")
        df = df.append({'link': main_link+sublink, 'Title/Address': title, 'img_links': img_links, 'price': price, 'description': description, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'habital_area': habital_area, 'EPC certificate number': certicate_number, 'property_type': property_type, 'score': score}, ignore_index=True)


df.to_csv('Knokke_realo.csv')