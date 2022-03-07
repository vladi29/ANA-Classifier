#Caracas 06/02/2022

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

raw_url= "https://www.anapatterns.org/"
patterns = range(0,30)
for pattern in patterns:
    images_url = "https://www.anapatterns.org/view_pattern.php?pattern={}".format(pattern)
    r = requests.get(images_url)
    html = r.content
    soup = bs(html, "html.parser")

    images = soup.find_all('a', class_='grouped_elements')

    i = 0
    for image in images:
        i += 1
        #img_src = image.get('href')  #Imagenes con marca de agua 
        img_src = image.find('img').get('src')  #Imagenes sin marca de agua
        img = requests.get(raw_url + img_src)
        img_name = "AIDA_Dataset/" + "{}_".format(pattern) + str(i) + ".jpg"
        with open(img_name, 'wb') as imagen:
            imagen.write(img.content)
