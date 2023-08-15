import math
 
# A function to print all prime factors of
# a given number n
def primeFactors(n):
    li=[]
    # Print the number of two's that divide n
    while n % 2 == 0:
        li.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            li.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        li.appned(n)
    return li

for aa in range(int(input())):
    n=int(input())
    x= primeFactors(n)
    d={}
    for i in x:
        if(i in x):
            d[i]+=1
        else:
            d[i]=1
    p=[]
    f=[]
    z=0
    for i in d:
        f.append(i)
        p.append(d[i])
        if(d[i]!=1):
            z=1
    
    if(z==0):
        prin

    