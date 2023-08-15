# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())
    s=input()
    c=0
    k=s
    for i in range(m):
        l,r=map(int,input().split())
        l-=1
        r-=1
        s=s[:l]+s[r::-1]+s[r+1:]
      