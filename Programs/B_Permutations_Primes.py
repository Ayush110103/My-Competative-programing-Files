import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    # li=list(map(
    # int,input().split()))
    h=[]
    if(n==1):
        print(1)
        continue
    if(n==2):
        print(2,1)
        continue
    x=[]
    for i in range(n):
        h.append(0)
    h[0]=2
    h[n//2]=1

    h[n-1]=3
    for i in range(n):
        x.append(0)
    p=4
    for i in range(1,n-1):
        if(i==n//2):
            continue
        h[i]=p
        p+=1
    
    print(*h) 

    
        
    
         