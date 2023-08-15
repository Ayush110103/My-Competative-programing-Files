# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    k=li.copy()
    k.sort()
    z=0
    for i in range(n):
        if(li[i]%2==k[i]%2):
            continue
        else:
            z=1
            break
    if(z==0):
        print("YES")
    else:
        print("NO")
            