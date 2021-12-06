# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:37:11 2021

@author: User
"""
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
t = np.array([[True,True,False],[False,False,True]])

s = sum(x[t])