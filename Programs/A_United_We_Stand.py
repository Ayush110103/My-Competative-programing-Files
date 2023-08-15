# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    b=[]
    c=[]
    k=max(li)
   
    # print(n-1,1)
    for i in range(n):
        if(li[i]==k):
            c.append(li[i])
        else:
            b.append(li[i])
    if(b==[]):
        print(-1)
        continue
    else:
        print(len(b),len(c))
        print(*b)
        print(*c)
