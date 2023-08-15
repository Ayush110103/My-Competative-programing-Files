# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    e,o=0,0
    if(n==1):
        print("NO")
        continue
    for i in li:
        if(i%2==0):
            e+=1
        else:
            o+=1
    if(o%2!=0):
        print("NO")
        continue
    print("YES")