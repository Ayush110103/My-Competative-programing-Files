# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    if(k==1):
        x=[]
        for i in range(n):
          x.append(i+1)
        print(*x)
    for i in range(n):
        if(li[i]%k==0):
            li[i]==k
            continue
        li[i]=li[i]%k
    p=[]
    for i in range(n):
        p.append([li[i],-(i+1)])
    
    p.sort()
    p.reverse()
    # print(max(p))
    print(p)
    for i in range(n):
        li[i]=-1*p[i][1]
    print(*li)