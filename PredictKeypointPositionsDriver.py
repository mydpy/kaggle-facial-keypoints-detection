# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:48:41 2015

@author: mbaker
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
        

        

        


