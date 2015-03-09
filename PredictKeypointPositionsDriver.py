# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:48:41 2015

@author: mbaker
"""

"""
import numpy as np
from scipy.misc import *
from PIL import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
a = training[1]
image = a[30]
image = image.split(" ")
image2 = np.reshape(image, (96,96))
image2 = image2.astype(np.float)
imgplot = plt.imshow(image2, cmap = cm.Greys_r)
"""








import csv
import numpy as np


training = {}
test = {}
lookup = {}


with open('data/training/training.csv', 'rb') as train_csv:
    reader = csv.reader(train_csv)
    key = 0    
    for row in reader:
        training[key] = row
        key = key + 1
        
with open('data/test/test.csv', 'rb') as test_csv:
    reader = csv.reader(test_csv)
    key = 0    
    for row in reader:
        test[key] = row
        key = key + 1
        
        
with open('data/IDLookupTable.csv', 'rb') as ids_csv:
    reader = csv.reader(ids_csv)
    key = 0    
    for row in reader:
        lookup[key] = row
        key = key + 1
        

        

        


