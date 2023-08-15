for aa in range(int(input())):
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    x=[]
    s=0
    for i in range(n):
        s+=li[i]
        x.append(s)
    

    g=x[m-1]
    if(min(x)==g):
        print(0)
        continue
    ####
    ne=[]
    p=[]
    for i in range(n):
        if(li[i]<0):
            ne.append(i)
    for i in range(n):
        if(li[i]>0):
            p.append(i)
    f=g
    w=0
    c=0
    z=0
    for i in range(0,m):
        w+=li[i]
        if(w<g):
            if(li[m-1]>0):
                li[m-1]=-1*li[m-1]
                c+=1
                z=1
                break
    
    if(z==1):
        for i in range(m-1,n):
            x[i]+=2*li[m-1]
    


    # for i in range(m,n):
    #     f+=li[i]
    #     if(f<g):





