import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,k,g=map(int,input().split())
    # li=list(map(int,input().split()))
    li=[]
    limit=g//2
    t=k*g
    if(t<n):
        print(t)
        continue
    x=t//n
    r=x%g
    if(n==2 and r==g//2):
        print(0)
        continue
    if(r<g//2):
        if(x//g==0):
            print(t)
            continue
        else:
            print(g)
            continue
    


    
        
        
    



