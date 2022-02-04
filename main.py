# Universidad Simon Bolivar - 26 de Enero de 2022
# Trabajo final de grado: Clasificador de patrones ANA
# Vladimir Alfaro - 1510023

# Creacion, entrenamiento, validacion y prueba de la red

import torch.nn as nn
import torch.nn.functional as F
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import os

#----------Paths----------

labels_path = 'labels.csv'
images_path = 'images.npz'

labels = pd.read_csv(labels_path)
labels = labels.values.tolist()

images = np.load(images_path)
images = images['arr_0']

images_list = []
labels_list = []

A = random.randint(0, 2079)
images_list.append(images[A])
labels_list.append(labels[A])

B = random.randint(0, 2079)
images_list.append(images[B])
labels_list.append(labels[B])

C = random.randint(0, 2079)
images_list.append(images[C])
labels_list.append(labels[C])

D = random.randint(0, 2079)
images_list.append(images[D])
labels_list.append(labels[D])

E = random.randint(0, 2079)
images_list.append(images[E])
labels_list.append(labels[E])

F = random.randint(0, 2079)
images_list.append(images[F])
labels_list.append(labels[F])

for i in range(0,6):
    plt.subplot(2,3, i+1)
    imagen = images_list[i]
    print("Label: ", labels_list[i])
    plt.imshow(imagen)
plt.show()