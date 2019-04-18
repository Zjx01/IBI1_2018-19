# What does this piece of code do?
# Answer:this code is used to find prime numbers 

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint
#pick random numbers

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
#to make u a integer
    for i in range(2,u+1):
        if n%i == 0:
            p=False
        else:
            p=True
#n doet not have common factor except 1 and itslef          


     
print(n)



