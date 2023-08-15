import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    j=0
    n,m,k=map(int,input().split())
    p,q=map(int,input().split())
    
    for i in range(k):
        o,t=map(int,input().split())
        if(abs(p-o)+abs(q-t))%2==0:
            j=1
            
    
    if(j==0):
        print("YES")
    else:
        print("NO")