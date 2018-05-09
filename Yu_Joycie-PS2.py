
# coding: utf-8

# In[54]:


# Numpy is a library for working with Arrays
import numpy as np
print("Numpy version:        %6.6s (need at least 1.7.1)" % np.__version__)

# Pandas makes working with data tables easier
import pandas as pd
print("Pandas version:       %6.6s (need at least 0.11.0)" % pd.__version__)

# SciPy implements many different numerical algorithms
import scipy as sp
print("SciPy version:        %6.6s (need at least 0.12.0)" % sp.__version__)

import scipy.sparse
import csv


# In[56]:



# define constants
alpha = 0.85
epsilon = 0.00001


# In[79]:


# 1.2 create adjacency matrix
# function that takes in file name and outputs a matrix
# reads each line of the file and splits it
def data_input (file):
    # create empty matrix with size matching # unique articles 
    matrix = np.zeros(shape = (10748,10748), dtype = 'int')
    with open(file, 'r') as file:
        content = file.readlines()
        for line in content :
            text = line.split(", ") # returns array
            textNum = [int(num) for num in text]
            matrix[textNum[0], textNum[1]] = textNum[2]
    return matrix


matrix = data_input('links.txt')


# In[84]:


# 1.3 modify adjacency matrix
# Set diagonal to zero
np.fill_diagonal(matrix, 0)

col_sums = np.sum(matrix, 0) 
col_sums = [1 if x == 0 else x for x in col_sums]
H = np.divide(matrix, col_sums, dtype='float')


# In[99]:


# 1.4 identify dangling nodes
dang_sums = np.matrix(1 - np.sum(H, 0))


# In[129]:


# 1.5 calculate influence vector

# create article vector with shape (n, 1)
# assume all publications produce only 1 article making the total 10748
total = 10748
row_total = np.sum(matrix, 1)
A_tot = np.matrix(np.divide(row_total, total, dtype="float")).T

# make initial start vector where shape is (n, 1) with values 1/# of articles
pi_k = np.empty(10748); start.fill(1/10748)
pi_k = np.matrix(start)


#π(k+1) =αHπ(k) +[αd.π(k) +(1−α)]a

# calculate influence vector
def sparse_eq (d, H, a, pi_k) :
    # define constants
    alpha = 0.85
    epsilon = 0.00001
    pi_k = alpha * np.dot(H, pi_k) + np.dot(alpha * np.dot(pi_k, d) + (1-alpha), a) 
    total = np.sum(np.sum(pi_k))
    pi_k = np.divide(pi_k, total)
    return pi_k

pi_k = sparse_eq(dang_sums, H, A_tot, pi_k)
pi_k.shape 
#H.shape (10748, 10748)
#dang_sums.shape (1, 10748)
#A_tot.shape (10748, 1)


# In[ ]:


# 1.6 calculate eigenfactor

