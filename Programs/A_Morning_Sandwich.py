# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m,k=map(int,input().split())
    # li=list(map(int,input().split()))
    t=m+k
    if(t>=n):
        print(2*n-1)
    else:
        print(2*t+1)
    