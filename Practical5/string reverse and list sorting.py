# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:04:05 2019

@author: Jessi
"""
#print(sorted("This is a test string from Andrew".split(), key=str.lower))


s=input()
s=s[::-1]
s=sorted(s.split())
s.reverse()
print(s)


s=input()
s=s[::-1]
print(sorted(s.split()).reverse())






