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

sapo = "https://www.luxuryestate.com/belgium/flanders/west-flanders-province/arrondissement-brugge/knokke-heist"
response = get(sapo, headers=headers)

html_soup = BeautifulSoup(response.content, 'html.parser')

df = pd.DataFrame(columns=['link', 'title', 'description',
                           'price', 'details', 'img_links', 'tags'])

container = html_soup.find_all('li', class_="clearfix")
for i in container:
    # img = i.find('img')
    # img_alt = img['alt']
    # img_link = img['src']
    # img_count = (i.find('span', class_="image-count")).text
    # print(img_link, im    g_count, img_alt)
    # print()
    link = i.find('a', class_="js_clickable")
    link = link['href']
    response2 = get(link, headers=headers)
    html_soup2 = BeautifulSoup(response2.content, 'html.parser')
    title = (html_soup2.find('h1', class_="title-property")).text

    description = html_soup2.find('p', class_="description")
    description = (description.find('span')).text.strip()

    price = (html_soup2.find('div', class_="price")).text.strip()

    details_container = html_soup2.find('div', class_="general-features")
    details_nodes = details_container.find_all('div', class_="short-item")

    details = []

    for node in details_nodes:
        key = (node.find('span')).text.strip()
        value = (node.find('div')).text.strip()
        details.append(key + ": " + value)

    img_links = []
    img_links.append(
        (html_soup2.find('div', class_="picture--big"))['data-src'])
    temp = html_soup2.find_all('div', class_="picture--small")
    img_links.append(temp[0]['data-src'])
    img_links.append(temp[1]['data-src'])

    tags = []
    temp = html_soup2.find_all('span', class_="breadcrumb-name")
    for j in temp:
        tags.append(j.text.strip())
    
    df = df.append({'link': link, 'title': title, 'description': description,
               'price': price, 'details': details, 'img_links': img_links, 'tags': tags}, ignore_index=True)


print(df)
df.to_csv('./csvs/Knokke_luxury_estate.csv')