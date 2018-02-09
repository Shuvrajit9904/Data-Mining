#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 23:41:00 2018

@author: shuvrajit
"""

import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import time
#random.seed(seed = 57)

start_time = time.time()
n = 250

#Problem A
#Generate random numbers in the domain [n] 
#until every value i ∈ [n] has had one random number equal to i. 
#How many random trials did this take? We will use k to represent this value


def getK(n):
    k = 0
    arr = [0 for i in range(n)]
    #r1 = random.randint(0,n)
    #arr[r1] = True
    ct = 0
    while(1):
        k += 1
        r1 = random.randint(0,n)
        if arr[r1] >= 1:
            arr[r1] += 1
        else:
            ct += 1
            arr[r1] = 1
        if ct == n:
            break
    return k
k = getK(n)

print("Q1A. This took {} random trials.".format(k))


#Problem B
#Repeat step A for m = 300 times, 
#and for each repetition record the value k of how many random trials
#we required to collect all values i ∈ [n]. 
#Make a cumulative density plot as in 1.B.

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
#Use the above results to calculate the empirical expected value of k

ksum = df2.sum()['k']
estimate = ksum /float(m)
    
print(
    'The expected number of k is {}'
      .format(estimate))


#Problem D
#Describe how you implemented this experiment and 
#long it took for n = 250 and m = 300 trials.
#Show a plot of the run time as you gradually increase the parameters n and m. 
#(For at least 3 fixed values of m between 300 and 5,000, 
#plot the time as a function of n.) 
#You should be able to reach n = 20,000 and m = 5,000

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

N = [250, 500, 1000, 2000, 5000, 10000, 20000]


M = [300, 1000, 2000, 5000]
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
plt.legend(['m = 300','m = 1000','m = 2000','m = 5000'], loc = 'upper left')
plt.show()



