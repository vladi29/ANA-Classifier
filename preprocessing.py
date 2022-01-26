# Universidad Simon Bolivar - 21 de Enero de 2022
# Trabajo final de grado: Clasificador de patrones ANA
# Vladimir Alfaro - 1510023

# Preprocesamiento de las imagenes

import matplotlib.pyplot as plt
import pandas as pd
import os
from natsort import os_sorted
import cv2
import random

def preproccessing_training(Labels_path, Images_path):

    data = pd.read_excel(Labels_path)
    labels_list = data['StainingPatterns'].values.tolist()
    images = data['ImageFileName'].values.tolist()

    images_list = []
    for image in images:
        print(image)
        image_path = images_path + '/' + image
        image = cv2.imread(image_path)
        image = (image/255).astype('float32')
        image = cv2.resize(image, (100, 75))
        images_list.append(image)

    return labels_list, images_list

    # aux = ''
    # patterns = {}
    # for pattern in labels_list:
    #     if pattern != aux:
    #         patterns[pattern] = labels_list.count(pattern)
    #         aux = pattern
    #     else:
    #         continue
    # #print(patterns)
    # print('Numero de patrones en el dataset: ', len(patterns))
