# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:26:49 2015

@author: mbaker
"""
import csv
import math
        
class PredictKeypointPosition:
    def __init__(self, data_path, test_path='', id_path=''):
        self.data = {}
        self.train = {}
        self.residual = {}
        self.test = {}
        self.id = {}
        self.__populate(data_path, test_path, id_path)
    
    def populate(self, data_path, test_path, id_path):
        self.load(data_path)
        self.load(test_path)
        self.load(id_path)
        self.create_training_class(.80)
        
    def load(self, path):
        if path == '': return
        with open(path, 'rb') as test_csv:
            reader = csv.reader(test_csv)
            key = 0    
            for row in reader:
                self.data[key] = row
                key = key + 1
    
    def update(self, newdata):
        self.data = newdata
    
    def create_training_class(self, percent):
        total_size = len(self.data)      
        train_size = int(math.floor(total_size*percent))
        for i in range(train_size):
            self.train[i] = self.data[i]
        for i in range(train_size, total_size):
            self.residual[i] = self.data[i]

    __populate = populate