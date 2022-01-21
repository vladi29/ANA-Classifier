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

data_path = r"C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/AIDA_HEp-2_GroundTruth.xls"
data = pd.read_csv(data_path, on_bad_lines = 'skip')
print(data)


