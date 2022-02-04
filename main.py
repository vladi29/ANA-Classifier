# Universidad Simon Bolivar - 26 de Enero de 2022
# Trabajo final de grado: Clasificador de patrones ANA
# Vladimir Alfaro - 1510023

# Creacion, entrenamiento, vlaidacion y entrenamiento de la red

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
from preprocessing import preprocessing_training as ppt

# Paths

labels_path = 'labels.csv'
images_path = 'images.npz'

#labels, images, names = ppt(labels_path, images_path)

# images_list = []
# labels_list = []
# names_list = []

# A = random.randint(0, 2079)
# images_list.append(images[A])
# names_list.append(names[A])
# labels_list.append(labels[A])

# B = random.randint(0, 2079)
# images_list.append(images[B])
# names_list.append(names[B])
# labels_list.append(labels[B])

# C = random.randint(0, 2079)
# images_list.append(images[C])
# names_list.append(names[C])
# labels_list.append(labels[C])

# D = random.randint(0, 2079)
# images_list.append(images[D])
# names_list.append(names[D])
# labels_list.append(labels[D])

# E = random.randint(0, 2079)
# images_list.append(images[E])
# names_list.append(names[E])
# labels_list.append(labels[E])

# F = random.randint(0, 2079)
# images_list.append(images[F])
# names_list.append(names[F])
# labels_list.append(labels[F])

# for i in range(0,6):
#     plt.subplot(2,3, i+1)
#     imagen = images_list[i]
#     print("Name: ", names_list[i])
#     print("Label: ", labels_list[i])
#     plt.imshow(imagen)
# plt.show()