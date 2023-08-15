for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    k=li.copy()
    k.sort()
    if(li==k):
        print(0)
        continue
    d={}
    f={}
    for i in range(n):
        d[li[i]]=i
    for i in range(n):
        f[k[i]]=i
    max=0
    s=1
    e=0
    q=[]
    w=[]
    for i in d:
        c=abs(f[i]-d[i])
        if(max==c):
           
            w.append(max(f[i],d[i]))
            if(f[i]==0 or d[i]==0):
                q.append(1)
            else:
                 q.append(min(f[i],d[i]))




        if(max<c):
            q=[]
            w=[]
            if(f[i]==0 or d[i]==0):
                q.append(1)
            else:
                 q.append(min(f[i],d[i]))
            w.append(max(f[i],d[i]))
        
        for i in range(len(q)):
        





