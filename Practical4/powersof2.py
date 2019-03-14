# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:50:36 2019

@author: Jessi
"""

#for simplicity, assume that x is no longer larger than 8129
#first choose a numben=7680r and find the biggest 2**n it contains,using function mode 2
# from the former code we can know that the biggest i is 12
#why this step cannot be calculated m=n-2**12

m=7680
i=13
answer= "7680="
while i>=0:
     if 2**i<m:
        m=m-2**i
        answer=answer + "+2**"+ str(i)
        i=i-1
     else:
        i=i-1
print (answer)
    

     
    




        




 

            
        
    
  
    
       











    
    




    

    
    
    
    


