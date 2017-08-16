# -*- coding: utf-8 -*-
# /usr/local/bin/python3

import numpy as np

simulacrums = np.array([])

def createSimulacrums(n=100, attrs=2):
    temp = np.random.random(n * attrs)
    RandomAttribute = temp.reshape(n, attrs)
    return RandomAttribute

def setWeight():
    pass