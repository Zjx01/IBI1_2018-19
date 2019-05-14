# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:24:54 2019

@author: Jessi
"""

import numpy as np
import matplotlib . pyplot as plt
from matplotlib import cm
"""
1 represent people  suscepticle to disease
0 represent people  infected
2 represent people recovered
"""
β=0.3
γ=0.05
B=[]
BB=[]
#the number of susceptible population vary acoording to the vaccinationrate 
#B is used to store the number of infectious people 
N=10000#sum of the population involved
for v in range(0,110,10):
    vaccinatedpopulation=v*N/100
    if N==vaccinatedpopulation:
       I=0
       S=0
       B=[0]
    else:
        vaccinatedpopulation=v*N/100
        I=1# people get ill
        S=10000-vaccinatedpopulation-I#people who is susceptible
        B=[1]
    R=0#people recovered
    for i in range(0,1000): #the time length=1000
        a=np.random.choice(range(2),int(S),p=[β*I/N,1-β*I/N])
        #susceptible individuals have chances to get disease and recover
        for j in a:
            if j==0:
                I=I+1#append the people newly infected and delete them from the susceptible populations
                S=S-1
            if j==1:
                S==S
        b=np.random.choice([2,0],I,p=[γ,1-γ])
        #infected individuals have chances to recover or stay ill
        for e in b:
            if e==2:
                R=+1#to append the newly recovered people and delete it in the infectious number
                I=I-1 
            if e==0:
                I==I
        B.append(I)#store the result of I for a vaccination rate
    BB.append(B)#to store infectious population of different vaccination rate
    B=[1]
        #plot
    #print('the number of infectious',B)
plt.figure(figsize=(6,4),dpi=150) 
for j in range(0,11):
    X=range(0,1001)
    f=plt.plot(X,BB[j],label=str(j*10)+'%',color=cm.gnuplot2(j*20))#the plot function is inside the loop, so it can be ploted in one figure
#plt.savefig ("markflow" ,type="png") 
#plt.plot(x, y, format_string, **kwargs): 
#x is the X-axis data, can be a list or array;Y in the same way;Format string for control curve, **kwargs second group or more (x, y, format_string)
plt.xlabel("times", fontsize=14)
plt.ylabel("number of people", fontsize=14)
plt.title("SIR model with different vaccination rates")
plt.legend() 
plt.show()
