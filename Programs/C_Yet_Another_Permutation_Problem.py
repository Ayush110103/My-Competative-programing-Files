# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    g=[0]*(n+4)
    g[1]=1
    a=[1]
    for i in range(1,n):
        t=i+1
        if(g[t]==1):
            continue
        if(g[t]==0):
            f=t
            while(f<=n):
                a.append(f)
                g[f]=1
                f=f*2
    print(*a)
            
              
