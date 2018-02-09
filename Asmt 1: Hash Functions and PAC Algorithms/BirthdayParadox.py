#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:14:57 2018

@author: shuvrajit
"""

import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import time
#random.seed(seed = 57)

start_time = time.time()
n = 4000

#Problem A
#Generate random numbers in the domain [n] until two have the same value. 
#How many random trials did this take? We will use k to represent this value.


def getK(n):
    k = 0
    arr = [False for i in range(n)]
    r1 = random.randint(0,n)
    arr[r1] = True
    while(1):
        k += 1
        r2 = random.randint(0,n)
        if arr[r2] == True:
            break
        else:
            arr[r2] = True
    return k
k = getK(n)

print("Q1A. This took {} random trials.".format(k))


#Problem B
#Repeat the experiment m = 300 times, 
#and record for each time how many random trials this took. 
#Plot this data as a cumulative density plot 
#where the x-axis records the number of trials required k, and 
#the y-axis records the fraction of experiments that succeeded (a collision) 
#after k trials. 
#The plot should show a curve that starts at a y value of 0, 
#and increases as k increases, and eventually reaches a y value of 1.

m = 300

count = []
count_trials = []
cumulative = [0 for i in range(m)]
fraction = [0 for i in range(m)]

for i in range(m):
    k = getK(n)
    count_trials.append(k)
    count.append(1)
single_end_time = time.time()

d = {'k': count_trials, 'count': count, 
     'cumulative': cumulative, 'Fraction': fraction}
df = pd.DataFrame(data = d)
df2 = df.sort_values(by = ['k'])
#df.groupby(by = ['k'])
np_df = df2.as_matrix()
np_df = np_df.astype(float)

for ind, rows in enumerate(np_df):
    if ind != 0:
        rows[2] = rows[1] + np_df[ind-1][2]
        rows[0] = float(rows[2]) / float(m)
    else:
        rows[2] = 1
        rows[0] = float(rows[2]) / float(m)

x = np_df[:,-1] #k
y = np_df[:, 0] #Cumulative Distribution

plt.plot(x, y)
plt.show()

#Problem C
#Empirically estimate the expected number of k random trials 
#in order to have a collision.
#That is, add up all values k, and divide by m.



ksum = df2.sum()['k']
estimate = ksum /float(m)
    
print(
    'The expected number of k random trials in order to have a collision is {}'
      .format(estimate))


#Problem D
#Describe how you implemented this experiment and 
#how long it took for m = 300 trials.
#Show a plot of the run time as you gradually increase the parameters n and m.
#(For at least 3 fixed values
#of m between 300 and 10,000, plot the time as a function of n.)
#You should be able to reach values of
#n = 1,000,000 and m = 10,000.

def getRandK(n1):
    k = 0
    r1 = random.randint(0,n1)
    while(1):
        k += 1
        r2 = random.randint(0,n1)
        if r1 == r2:
            break
    return k

first_time = single_end_time-start_time
print("Time taken for m=300 trials is {} seconds".format(first_time))

N = [4000,10000, 20000, 50000]
i = 100000
while i < 1000000:
    N.append(i)
    i += 100000


M = [300, 1000, 5000, 10000]
def getTime(N, m):
    times = []
    for n in N:
        print("This process is here for n = ", n)
        start_time = time.time()
        for i in range(m):
            k = getK(n)
        time_taken = time.time() - start_time        
        print("Time Taken: ", time_taken)
        times.append(time_taken)
    return times

delay = []
    
for m in M:
    print("m=",m)
    d1 = getTime(N,m)
    print(d1)
    delay.append(d1)

plt.plot(N,  delay[0])
plt.plot(N,  delay[1])
plt.plot(N,  delay[2])
plt.plot(N,  delay[3])
#plt.plot(N,  delay[4])
plt.legend(['m = 300','m = 1000','m = 5000','m = 10000'], loc = 'upper left')

plt.show()