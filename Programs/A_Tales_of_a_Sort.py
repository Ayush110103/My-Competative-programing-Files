# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    z=0
    mi=-1
    for i in range(n-1):
        if(li[i]>li[i+1]):
            z=1
            mi=max(mi,li[i])
    if(z==0):
        print(0)
        continue
    print(mi)
            
            
            