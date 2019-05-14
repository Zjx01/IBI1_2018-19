# What does this piece of code do?
# Answer:this code is used to find prime numbers between 1 and 100

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
    u = ceil(n**(0.5))#why we use it because a=b*c,n b and c must be located on the left and right side of the a*(0.5). so once we verify the one side we can know other side
#to make u a integer 
    for i in range(2,u+1):#to contain u in side of the range eg.25=5*5
        if n%i == 0:
            p=False
        
#n doet not have common factor except 1 and itslef          
print(n)



