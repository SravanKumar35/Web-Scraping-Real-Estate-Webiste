import requests
from bs4 import BeautifulSoup

url = 'https://www.rcsb.org/structure/1A69'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
pdb_id = url.split('/')[-1].lower()
images_location = "https://cdn.rcsb.org/images/rutgers/"
num_items = len( soup.select('#carousel-structuregallery .item') )
pdb_hash = pdb_id[1:3]

# print image urls to screen:

for i in range(num_items):
    # 0 = Asymmetric; 1+ = Biological Assembly
    if i == 0:
        img_url = images_location + pdb_hash + '/' + pdb_id + '/' + pdb_id + '.pdb-500.jpg'
    else:
        img_url = images_location + pdb_hash + '/' + pdb_id + '/' + pdb_id + '.pdb' + str(i) + '-500.jpg'
    print(img_url)