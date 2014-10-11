__author__ = 'Luke'

import numpy as np
from sklearn import cross_validation
from sklearn import datasets

iris = datasets.load_iris()
iris.data.shape, iris.target.shape

with open('workfile', 'w') as f:
    f.write('this is a test\n')
