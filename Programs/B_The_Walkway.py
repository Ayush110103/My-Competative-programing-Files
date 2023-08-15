# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def is_integer(n):
    return isinstance(n, float) and n.is_integer()
for aa in range(int(input())):
    # n=int(input())
    n,m,d=map(int,input().split())
    li=list(map(int,input().split()))
    c=math.ceil(n/d)
    print(c,"a")
    c=0
    i=0
    r=1
    while(i+1<m):
        t=r+d
        if(t>li[i] and t>li[i+1] ):
            c+=1
            r=li[i]
            i+=1
            continue
        else:
            break
            
    g=0
    for i in range(i,m):
        f=(li[i]-r)/d
        # print(f%1.0)
        if(f%1.0==0.0):
            continue
        else:
            g+=1

    if(g==0):
        print(c)
    else:
        print(c+g-1)
    

    
        