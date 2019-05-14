# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:06:38 2019

@author: Jessi
"""
import xml.dom.minidom
import re
import pandas as pd

filePath=r'C:/Users/Jessi/OneDrive/桌面/IBI/IBI1_2018-19/Practicum8'#Your file path
fileName='autophagosome.xlsx'
excel=filePath+'/'+fileName
re_store = re.compile(r'autophagosome')
#Function to find childnodes 
def Child(id, result):
    for term in terms:
        parents = term.getElementsByTagName('is_a')
        kid= term.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                result.add(kid)
                Child(kid, result)
                
#create a pandas.Dataframe to store the output
df = pd.DataFrame(columns=['id','name','definition','childnodes'])

#create the DOM tree    
DOMTree = xml.dom.minidom.parse("go_obo.xml")
obo = DOMTree.documentElement
terms = obo.getElementsByTagName('term') #get the nodelist of element term
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    if re_store.search(defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        result = set()#to avoid the repetitiness of the element we get
        Child(id, result)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(result)]})) 
        print(id, len(result))
#save to excel
df.to_excel(excel,index=False)

"""
abandoned method
---------------------------------
content="<defstr>(.*?)</defstr>"
for a in term:
    id=[]
    name=[]
    definition=[]
    if re.match(r'<id>(.*?)</id>',str(a)):
        id.append()
        #incorrect <>
    if re.match(r'<name>(.*?)</name>',str(a)):
        name.append() 
    for content in a:
        #'element' object is not iterable
        if re.match(r'autophagosome',content):
           definition.append()
           #use dom instead of regular expression
    print(name)
    print(id)
    print(definition)
#collectchildrenGoIDSER(GOID,resultSet)
def children_id(GOID):
    count=0
    res=data.getElementByTagName("is_a")
    for e in res:
        count=count+1
        for element in res:
"""
            
            
    
            
            
        
        
        
        
    
    


                   
            
               
           
           
           
           
        
   
        
    
    
    
    
        
        
        
        
        