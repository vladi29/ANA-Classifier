# Universidad Simon Bolivar - 21 de Enero de 2022
# Trabajo final de grado: Clasificador de patrones ANA
# Vladimir Alfaro - 1510023

# Preprocesamiento de las imagenes

import pandas as pd
import time
import cv2
import random
import numpy as np

#----------Preprocessing of training and validation dataset----------

labels_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/AIDA_HEp-2_GroundTruth.xlsx'
images_path = 'C:/Users/Usuario/OneDrive/Escritorio/Tesis/Datasets/AIDA_HEp-2_DB_publico/aida_project_database'

df = pd.read_excel(labels_path, header = 0)
shuffled_df = df.sample(frac = 1)
shuffled_df.reset_index(drop = True, inplace = True)
shuffled_df.to_excel('shuffled_images.xlsx')

data = pd.read_excel('shuffled_images.xlsx')
labels_list = data['StainingPatterns'].values.tolist()
images = data['ImageFileName'].values.tolist()

start_time = time.time()
images_list = []
for image in images:
    print(image)
    image_path = images_path + '/' + image
    image = cv2.imread(image_path)
    image = (image/255).astype('float32')
    image = cv2.resize(image, (100, 75))
    images_list.append(image)
final_time = time.time() - start_time
print('Tiempo de preprocesado de las images:', final_time/60)

labels = np.asarray(labels_list)
np.savetxt('labels.csv', labels, fmt ='%s', delimiter = ',')

names = np.asarray(images)
np.savetxt('names.csv', names, fmt ='%s', delimiter = ',')

images_compressed = np.asarray(images_list)
np.savez_compressed('images.npz', images_compressed)


#----------Get all labels----------
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

#----------Preprocessing of test dataset----------
