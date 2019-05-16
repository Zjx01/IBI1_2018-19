# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:02:27 2019

@author: Jessi
"""
DNA_sequence=input("input the DNA sequence:" )
my_dic={}
for word in DNA_sequence:
    if word in my_dic:
        my_dic[word]+=1
    else:
        my_dic[word]=1
print(my_dic)#if the word is in the dictionary, the value+1, else import the way into the dictionary add the key and its value=1
import matplotlib.pyplot as plt
labels=list(my_dic.keys())#the label varys according to the sequence you input
size=my_dic.values()
plt.pie(size,labels=labels,autopct='%1.1f%%')
plt.show()
#when run the program,the content need to be typed in by yourself, after which you should press the button enter 





    
            
            

