# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    a,b,c=map(int,input().split())
    # li=list(map(int,input().split()))
    if(a>b):
        print("First")
        continue
    if(b>a):
        print("Second")
        continue
    if(c%2==0):
        print("Second")
        continue
    print("First")
    
    

