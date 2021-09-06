#!/usr/bin/env python
# coding: utf-8

# In[4]:



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = int(input("Parameter of Interst:(1:MSE  2:Bias  3:Variance) "))
B = int(input("Graph with respect to:(1:K  2:N(Ab)) "))

if A == 1: 
    P = "MSE"
if A == 2:
    P = "Bias"
if A == 3:
    P = "Variance"
    
if B == 1:
    Q = "k"
    legend = ["Kd = 10^-0", "Kd = 10^-1", "Kd = 10^-2", "Kd = 10^-3", "Kd = 10^-4", "Kd = 10^-5", "Kd = 10^-6", "Kd = 10^-7", "Kd = 10^-8", "Kd = 10^-9" ,"Kd = 10^-10"]
if B == 2:
    Q = "n"
    legend = ["N = Mmax", "N = 2*Mmax", "N = 3*Mmax", "N = 4*Mmax", "N = 5*Mmax", "N = 6*Mmax", "N = 7*Mmax", "N = 8*Mmax", "N = 9*Mmax", "N = 10*Mmax"]

if B == 1:
    data0 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}0.csv".format(Q))
data1 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}1.csv".format(Q))
data2 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}2.csv".format(Q))
data3 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}3.csv".format(Q))
data4 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}4.csv".format(Q))
data5 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}5.csv".format(Q))
data6 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}6.csv".format(Q))
data7 = pd.read_csv("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/{}7.csv".format(Q))

if B == 1:
    max0 = np.max(data0["{}".format(P)])
max1 = np.max(data1["{}".format(P)])
max2 = np.max(data2["{}".format(P)])
max3 = np.max(data3["{}".format(P)])
max4 = np.max(data4["{}".format(P)])
max5 = np.max(data5["{}".format(P)])
max6 = np.max(data6["{}".format(P)])
max7 = np.max(data7["{}".format(P)])

plt.figure(figsize=(10, 10), dpi = 500)

plt.title("{} as a function of M(Ag) for different {}".format(P,Q), fontsize = 18)

if B == 1:
    x0 = data0["AG"].astype(str).astype(float)
    y0 = data0["{}".format(P)].astype(str).astype(float)
    realy0 = y0/max0

x1 = data1["AG"].astype(str).astype(float)
y1 = data1["{}".format(P)].astype(str).astype(float)
realy1 = y1/max1

x2 = data2["AG"].astype(str).astype(float)
y2 = data2["{}".format(P)].astype(str).astype(float)
realy2 = y2/max2

x3 = data3["AG"].astype(str).astype(float)
y3 = data3["{}".format(P)].astype(str).astype(float)
realy3 = y3/max3

x4 = data4["AG"].astype(str).astype(float)
y4 = data4["{}".format(P)].astype(str).astype(float)
realy4 = y4/max4

x5 = data5["AG"].astype(str).astype(float)
y5 = data5["{}".format(P)].astype(str).astype(float)
realy5 = y5/max5

x6 = data6["AG"].astype(str).astype(float)
y6 = data6["{}".format(P)].astype(str).astype(float)
realy6 = y6/max6

x7 = data7["AG"].astype(str).astype(float)
y7 = data7["{}".format(P)].astype(str).astype(float)
realy7 = y7/max7

plt.xlabel("AG", fontsize = 12)
plt.ylabel("{}/Max({})".format(P,P), fontsize = 12)

if B == 1:
    plt.plot(x0, realy0, "-")
plt.plot(x1, realy1, "-")
plt.plot(x2, realy2, "-")
plt.plot(x3, realy3, "-")
plt.plot(x4, realy4, "-")
plt.plot(x5, realy5, "-")
plt.plot(x6, realy6, "-")
plt.plot(x7, realy7, "-")

plt.legend(legend)

plt.savefig("/Users/ljs233233/Desktop/Files/Summer2021/Biosensor/Datafolder/divmax{}_{}.png".format(P,Q))
plt.show()


# # data.max()

# In[54]:


np.argmax(data["MSE"])


# In[43]:


np.argmax(data["MSE"])


# In[ ]:





# In[ ]:




