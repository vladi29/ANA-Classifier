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

# Paths

images_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/aida_project_database'
labels_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/AIDA_HEp-2_GroundTruth.xlsx'
