# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:20:38 2019

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
B=[1]
BB=[]
#the number of susceptible population vary acoording to the vaccinationrate 
I=1# people get ill
R=0#people recovered
#A,B,C are used to store the length of infectious and recovered people
N=10000#sum of the population involved
vaccinationrate=np.arange(0.1,1.1,0.1)
vaccinationrate.tolist() 
#print(vaccinationrate)
for v in vaccinationrate:
    vaccinatedpopulation=v*N-1
    S=9999-vaccinatedpopulation#people who is susceptible
    for i in range(0,1000): #the time length
        a=np.random.choice(range(2),int(S),p=[β*S/N,1-β*S/N])
        #susceptible individuals have chances to get disease and recover
        for j in a:
            if j==0:
                I=I+1#append the people newly infected and delete them from the susceptible populations
                S=S-1
            if j==1:
                S==S
                I==I
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
    for element in  BB:  
        X=range(0,1001)
        #plt.plot(x, y, format_string, **kwargs): 
        #x is the X-axis data, can be a list or array;Y in the same way;Format string for control curve, **kwargs second group or more (x, y, format_string)
        f=plt.plot(X,element)#the plot function is inside the loop, so it can be ploted in one figure
plt.figure(figsize=(6,4),dpi=150)    
plt.xlabel("times", fontsize=14)
plt.ylabel("number of people", fontsize=14)
plt.title("SIR_vaccination")
plt.legend([v in vaccinationrate],loc='upper right')
plt.savefig ("markflow" ,type="png")         
plt.show()



    