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

labels_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/AIDA_HEp-2_GroundTruth.xlsx'
images_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/aida_project_database'

labels, images, names = ppt(labels_path, images_path)

random_number = random.randint(0, 2079)
print("Name: ", names[random_number])
print("Label: ", labels[random_number])
plt.imshow(images[random_number])
plt.show()