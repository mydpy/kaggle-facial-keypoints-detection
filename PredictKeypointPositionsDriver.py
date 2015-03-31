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


import numpy as np
import PredictKeypointPositions as pkp
reload(pkp)

training_path = 'data/training/training.csv'
test_path = 'data/test/test.csv'
lookup_table_path = 'data/IDLookupTable.csv'

a = pkp.PredictKeypointPosition(training_path)

        

        


