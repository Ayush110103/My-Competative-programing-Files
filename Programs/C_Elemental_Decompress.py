for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    if(n not in li):
        print("NO")
        continue
    p=[]
    q=[]
    d={}
    u=[]
    v=[]
    for i in range(n+1):
        v.append(0)
        u.append(0)
    for i in range(n):
        p.append(0)
        q.append(0)


    for i in range(n):
        d[i+1]=2
    f={}
    for i in range(n):
        if(li[i] in f):
            f[li[i]]+=1
        else:
            f[li[i]]=1
    z=0
    c=0
    x=[]
    for i in f:
        if(f[i]==2):
            c+=1
        if(f[i]>2):
            z=1
            break
        # if(f[i]==2 and (i==1 or i==2)):
        #     z=1
        #     break
    
    for i in f:
        x.append(i)
    if(z==1):
        print("NO")
    
    t=1

    # print(d)
    for i in range(n):
        if(f[li[i]]==1):
            p[i]=li[i]
            d[li[i]]-=1
            continue

        if(f[li[i]]==2 and d[li[i]]==2):
            p[i]=li[i]
            d[li[i]]-=1
            q[i]=t
            u[t]=1
            continue
        if(f[li[i]]==2 and d[li[i]]==1):
            q[i]=li[i]
            d[li[i]]-=1
            p[i]=t
            u[li[i]]=1
            t+=1
            continue
    # print(p)
    # print(q)
    if( 0 not in q):
        print("YES")
        print(*p)
        print(*q)
    v=[]
    r=[]
    e=[]
    for i in range(1,n+1):
        if(u[i]==0):
           r.append(i)
    r.sort()
    for i in range(n):
        if(q[i]==0):
            e.append(p[i])
    l={}
    for i in range(len(e)):
        l[e[i]]=i
    e.sort()
    t={}
    z=0
    for i in range(len(r)):
        if(r[i]<=e[i]):
          t[e[i]]=r[i]
        else:
            z=1
            break
    if(z==1):
        print("NO")
        continue


    for i in range(n):
        if(f[li[i]]==1):
            q[i]=t[p[i]]
    print("YES")
    print(*p)
    print(*q)
    
    
    
          

        

    # for i in range(n):
       
    #     if(u[i+1]==0):
    #         r.append(i+1)
    # for i in range(n):
    #     if(f[li[i]]==1):
    #         if(u[li[i]]==0):
    #             q[i]=li[i]
    #             u[li[i]]=1
    #         else:
    #           while(u[li[i]]!=0):
    #             o=1
    #             if(u[li[i]-o]==0):
    #                 q[i]=li[i]-o
    #                 u[li[i]-o]=1
    #             o+=1
    # for i in range(n):
    #     if(q[i]==0):
    #         print("NO")
    #         continue
    # print("YES")
    # print(p)
    # print(q)
        


   

    


    




    
