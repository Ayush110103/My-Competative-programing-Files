
import math
def primeF(n):
    r=[]
    while n % 2 == 0:
        r.append(2),
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            r.append(i),
            n = n // i
    if n > 2:
        r.append(n)
    return r
for i in range(int(input())):    
    n=int(input())
    li=primeF(n)
    u={}
    for i in li:
        u[i]=0
    for i in li:
        u[i]+=1
    t=0
    
    k=[]
    l=[]
    
    
    
    ats=0
    for i in u:
        ats=max(ats,u[i])
    
    while(ats):
        hh=1
       
        for j in u:
            if u[j]>0:
                    hh=hh*j
                    u[j]=u[j]-1
            
                
        t=t+hh
        ats-=1
    # k[]=44*66
    
    
    print(t)