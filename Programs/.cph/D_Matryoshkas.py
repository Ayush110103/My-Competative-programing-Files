for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    d={}
    for i in li:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    c=0

    x=[]
    y=[]
    for i in d:
    
        x.append(i)
        y.append(d[i])
    # z=0
    # if(x[0]>x[1]):
    #     z=1
    # else:
    #     z=0
    # for i in range(1,len(y)-1):
    #     if(z=0):
    #         if(y[i+1]-y[i]>=0):



    #         if(y[i+1]-y[i]<0):




    m=d[x[0]]
    n=y[i]
    if(y[1]>y[0]):
        
    for i in range(1,len(x)):
        if(x[i]-x[i-1]>1):

            c+=m
            # print(m)vv
            m=0
            continue

        if(x[i]-x[i-1]==1):
            if(d[x[i]]>m):
                m=d[x[i]]
            if(y)
    
            
    
    c+=m

    # print(m)
    # print()
    print(c)





    
