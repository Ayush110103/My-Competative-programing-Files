import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    c=0
    d=0
    for i in range(n):
        if(li[i]%2==0):
            c+=1
        else:
            d+=1
  
    if(d>0):
        print(2**c)
    else: 
        print(2**c-1)
          