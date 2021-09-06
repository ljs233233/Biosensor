#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

filename = input("Filename: ")

mmax = int(input("Mmax: "))
m = np.arange(mmax - 1)
n = int(input("N: "))
kd = float(input("Kd: "))
v = 0.5
e0 = 8.85 * 10** -12
ncomp = m + ((m * v * kd)/(m - n))
 
p = np.zeros((len(m), len(m))) 
for j in range(len(m) - 1):
    p[j,j] = 1
    x = m[j]
    for i in range(j, 0, -1):
        if i == j - 1:
            p[j,i-1] = (p[j,i]*(kd**2)*(i) + p[j,i]*(n-i)*(x-i))/((n-i+1)*(x-i+1))
        else: 
            new = (p[j,i]*(kd**2)*(i) + p[j,i]*(n-i)*(x-i) - p[j,i+1]*(kd**2)*(i+1))/((n-i+1)*(x-i+1))
            p[j,i-1] = new
            
p_norm = []
for i in range(len(m)):
    norm = np.linalg.norm(p[i,:], ord = 1, axis = 0)
    value = p[i,:]/norm
    p_norm.append(value)

inds = np.argmax(p_norm, axis = 1)
nhat = m[inds]

# Bias
nmean = []
for i in (range(len(m))):
    nmean.append(np.inner(p_norm[i], nhat))
bias = nmean - m

# Variance
n2mean = []
for i in (range(len(m))):
    n2mean.append(np.inner(p_norm[i], (nhat ** 2)))
var = []
for i in range(len(m)):
    value = n2mean[i] - (nmean[i] ** 2)
    if value < 0:
        value = 0
    var.append(value)
    
# Mean Squared Error
mse = (bias**2) + (var)

# Store Data
data = pd.DataFrame()
data["AG"] = m
data["AB"] = n 
data["Complex"] = ncomp
data["Bias"] = bias
data["Variance"] = var
data["MSE"] = mse
data["AB"] = n


data.to_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}.csv".format(filename))


# In[ ]:




