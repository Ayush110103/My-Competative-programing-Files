for aa in range(int(input())):
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    p=1
    li.sort()
    li.reverse()
    g=[]
    for i in li:
        p*=i
    x=[]
    k=[]
    for i in range(10**5):
        g.append(0)
    for i in range(1,m+1):
        k.append(0)
        
        x.append(i)
    k.append(0)
    x.reverse()
    
    for i in range(m):

        if(sum(k)==m):
            r=i
            break
        if (p%x[i]==0):
            p=p/x[i]
            k[x[i]]=1
        
    if(sum(k)<m):
        print(-1)
        continue
    print()