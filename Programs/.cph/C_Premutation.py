for aa in range(int(input())):
    n=int(input())
    u=[]
    x=[]
    li=[]
    for i in range(n+1):
        u.append(0)
    for i in range(n):
        sub=list(map(int,input().split()))
        li.append(sub[0])

        x.append(sub)
    f={}
    for i in li:
        if(i in f):
            f[i]+=1
        else:
            f[i]=1
    for i in f:
        if(f[i]==1):
            l=i
        if(f[i]>1):
            r=i
    # print(f)
    k=x[li.index(l)]
    # print(k)
    t=[r]+k
    print(*t)
    


        


   