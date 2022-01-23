# Universidad Simon Bolivar - 21 de Enero de 2022
# Trabajo final de grado: Clasificador de patrones ANA
# Vladimir Alfaro - 1510023

# Preprocesamiento de las imagenes

import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from natsort import os_sorted
import cv2
import random

images_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/aida_project_database'
labels_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/AIDA_HEp-2_GroundTruth.xlsx'

data = pd.read_excel(labels_path)
labels_list = data['StainingPatterns'].values.tolist()
images = data['ImageFileName'].values.tolist()

aux = ''
patterns = {}
for pattern in labels_list:
    if pattern != aux:
        patterns[pattern] = labels_list.count(pattern)
        aux = pattern
    else:
        continue
#print(patterns)
print('Numero de patrones en el dataset: ', len(patterns))

images_list = []
for image in images:
    print(image)
    image_path = images_path + '/' + image
    image = cv2.imread(image_path)
    image = (image/255).astype('float32')
    image = cv2.resize(image, (100, 75))
    images_list.append(image)

random_image = random.randint(0, 2079)

print('Nombre: ', images[random_image])
plt.imshow(images_list[random_image])
plt.show()