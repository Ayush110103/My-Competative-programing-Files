for aa in range(int(input())):
    n=int(input())
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    d={}
    for i in li:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    t=0
    for i in d:
        if(t<d[i]):
            t=d[i]
    print(n-t)

