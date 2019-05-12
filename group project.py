# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:01:26 2019

@author: lenovo
"""

from collections import Counter
dna=input('Please input a DNA sequence:')
DNA=list(dna)
count=Counter(DNA) #get the number of each type of nucleotide
L=len(dna)
print('The GC content is:',(count['G']+count['C'])*100/L,'%')#to call the value of key 'C' & 'G' in dictionary count

DNA1=DNA[::]
cdna=DNA[::]
mRNA=DNA[::]
nuc=['A','G','C','T']
pair=['T','C','G','A']
mrna=['U','C','G','A']
#to store the basic nucleotide in the list for further corresponding
def basepair(x1,x2):
    for i in range(len(nuc)):
        for j in range(len(DNA1)):
            if DNA1[j] in nuc[i]:
                x1[j]=x2[i] 
    return x1
#for every nucleotide in the dna sequence, we found the same element in the nuc list, as its complementary element is stored in pair list.
#So each time we return element in pair list at the exact location of nucleu list 
#small example can be listed here
############ complementary dna
a=basepair(cdna,pair)        
print('The complementary DNA sequence is:',''.join(a[::-1]))
#join the separate nucleotides together according to the rule that transcription always start from the 5' primary end
#################    mrna
b=basepair(mRNA,mrna) 
mRNA=''.join(mRNA)      
print('The mRNA sequence is:',mRNA)

##############         mrna to protein

def translate(mRNA):
    #file=open('codon.txt','r')
    #codon=eval(file.read())
    codon={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L","UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UGU":"C", "UGC":"C", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", 
    "CUG":"L","CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", 
    "CAG":"Q","CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", 
    "AUG":"M","ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", 
    "AAG":"K","AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", 
    "GUG":"V","GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", 
    "GAG":"E","GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    #import the the dictionary of the amino acids exist in the natural world
    mRNA1=input('Please input a mRNA sequence:')
    if 'AUG' in mRNA1:   
      location=mRNA1.find('AUG')
      lmrna=[mRNA1[i:i+3] for i in range(location,len(mRNA1),3)]
      #the make it a intergrity of 3
      protein=['']*len(lmrna)
      #to set space for protein filling     
      k=list(codon.keys())
      v=list(codon.values())
      for i in range(len(k)):
          for j in range(len(lmrna)):
              if lmrna[j] in ['UAA','UAG','UGA']:
                  break
              #the stop codon
              elif lmrna[j] == k[i]:
                  protein[j]=v[i]
                 #if the jth element in the lmrna is equal to one of the keys in codon, the protein list store the value of the key
      print('The polypeptide sequence is:', ''.join(protein))
    else:
      print('This DNA sequence does not encode protein!')
    #file.close()
##################
"""
import sys
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
seq='TCGAGGGATCCAATTCGAATTCAAGCTTACGTAGCTGGATCCGGATCCGGATCC'
seql=list(seq)
#we separate the sequence into the list
diction={'AluI':['(TCGA)|(AGCT)','AGCT',2],'HindIII':['(AAGCTT)|(TTCGAA)','AAGCTT',1],'BamHI':['(GGATCC)|(CCTAGG)','GGATCC',1],'SalI':['(GTCGAC)|(CAGCTG)','GTCGAC',1]}
keys=list(diction.keys())
values=list(diction.values())


def location(seq,enzyme):
    index=keys.index(enzyme)
    fragment=[]
    loc=[]
    loca=set()
    rex=re.compile(values[index][0])
    for i in range(len(seq)-len(values[index][1])):
        fragment.append(seq[i:i+len(values[index][1])])
        for j in range(len(fragment)):
            if rex.search(fragment[j]):
                loc.append(j)
                loca=set(loc)
    return loca
                    

def digest(seql,location,enzyme):
    index=keys.index(enzyme)
    number=values[index][2]
    
    for i in location:
        seql.insert(i+number,'?')
    seq=str(''.join(seql))
    fragment=seq.split('?')
    return fragment
    
for i in keys:
    #print(location)
    seql=list(seq)
    
    locati=location(seq,i)
    fragment=digest(seql,locati,i)
    print(i,fragment)
    y_pos = np.arange(len(fragment))
    performance = [len(i) for i in fragment] 
    plt.bar(y_pos, performance, )
    plt.xticks(y_pos)
    plt.ylabel('bp')
    plt.title('DNA fragments')
     
    plt.show()   
"""
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#seq='TCGAGGGATCCAATTCGAATTCAAGCTTACGTAGCTGGATCCGGATCCGGATCCAAAAAGTCGACGCGCTTTCGCGATTTAGTCGTCGCAGCTAGTTTGCCAGAAGCGT'
#seq='AGCTTAAGCTTAAGCTTAAGCTTAAGCTTGGATCCGGATCCGTCGACGTCGAC'
#seq='AGCTGGGGGCT'
diction={'AluI':['AGCT',2],'HindIII':['AAGCTT',1],'BamHI':['GGATCC',1],'SalI':['GTCGAC',1]}#the distance to 5'
keys=list(diction.keys())
values=list(diction.values())

def digest(seql,location,enzyme):
    for i in location:
        seql.insert(i-1,'?')#insert ? befor i-1, that is exactly at the location of digestion    
    seq=str(''.join(seql))
    fragment=seq.split('?')
    return fragment

def location(seq,enzyme):
    index=keys.index(enzyme)
    number=values[index][1]#there are two things exist in the value
    length=len(values[index][0])
    fragment=[]#a list to store all the pieces of seq
    loc=[]#a list to store the location
    loca=set()
    rex=re.compile(values[index][0])    
    for i in range(len(seq)-length+1):#recognize from every nucleotide and +1 is because the characteristic of range 
        fragment.append(seq[i:i+length])#split the seq according to the sequence length of restriction enzyme for the later steps of recognition
    for j in range(len(fragment)):
        if rex.search(fragment[j]):
            loc.append(j+number+1)#get the index just before the location            
            loca=sorted(set(loc),reverse=True)#reverse the set so that when we insert the ?, the other won't be affected
    return loca
summary=[]    
for i in keys:  
    seql=list(seq)    
    loc=location(seq,i)
    if len(loc)==0:
        print("This DNA sequence can't be digested by",i)
    else:
        fragment=digest(seql,loc,i)
        summary.append(str(i)+':'+','.join(str(e) for e in loc))
        print(i,':',str(' / '.join(fragment)))
        #bar chart        
        fragments=(i+1 for i in range(len(fragment)))
        y_pos = np.arange(len(fragment))
        bplength = [len(i) for i in fragment] 
        plt.bar(y_pos, bplength)
        plt.xticks(y_pos,fragments)
        plt.ylabel('bp')
        plt.title('DNA fragments')     
        plt.show()   
print('The DNA is assumed to be linear. It can be digested by:')    
for e in summary:
    print(e)  
print('The number is the location of base (count from 1) after the restriction site')
 
    #diction={'AluI':['(?=(?P<AluI>AGCT))','AGCT',2],'HindIII':['(?=(?P<HindIII>AAGCTT))','AAGCTT',1],'BamHI':['GGATCC','GGATCC',1],'SalI':['(?=(?P<SalI>GTCGAC))','GTCGAC',1]}
