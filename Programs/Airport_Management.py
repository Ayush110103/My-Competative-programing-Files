import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d={}
    m=0
    for i in range(n):
        if(a[i] in d):
            d[a[i]]+=1
        else:
            d[a[i]]=1
        m=max(m,d[a[i]])
        if(b[i] in d):
            d[b[i]]+=1
        else:
            d[b[i]]=1
        m=max(m,d[b[i]])
    print(m)
        
        
        
        
        