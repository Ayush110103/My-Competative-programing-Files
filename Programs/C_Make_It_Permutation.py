for i in range(int(input())):    
    # c to remove
    n,c,f=(map(int,input().split()))
    li=list(map(int,input().split()))
    x=[]
    d={}
    p=0
    for i in li:
        if(i in d):
            d[i]+=1
            p+=1
        else:
            d[i]=1
    y=[]
    for i in d:
        y.append(i)
    y.sort()

    # for i in range(n+1):
    #     x.append(0)
    a=0
    if(1 not in y):
        a+=f
        y=[1]+y
        d[1]=1
        n=n+1
    # print(c,d[1])
    if(d[1]>1):
          a+=(d[1]-1)*c
    n=n-d[1]
    k=(max(y)-len(y))*f+p*c
    # print(k)
    if(k>n*c):
        a+=n*c
        print(a)
        continue
    for i in range(1,len(y)):
        # print(a)
        if(y[i]-y[i-1]>1):
          if((y[i]-y[i-1]-1)*f+(d[y[i]]-1)*c>n*c):
                a+=n*c
                # print(111)
                break
          else:
              a+=(y[i]-y[i-1]-1)*f
        a+=(d[y[i]]-1)*c
        n=n-d[y[i]]

    print(a)
    
        
          
        
            
    
    