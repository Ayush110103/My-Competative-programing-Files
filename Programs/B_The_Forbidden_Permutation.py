for i in range(int(input())):    
    n,m,p=(map(int,input().split()))
    li=list(map(int,input().split()))
    a=list(map(int,input().split()))
    k=[]
    d={}
    for i in range(n):
        d[li[i]]=i
    
    for i in a:
        k.append(d[i])
    c=[]
    for i in range(m-1):
        if(k[i]<k[i+1]<=k[i]+p):
            if(k[i]+p-k[i+1]<n-1-k[i+1]):
                c.append(min(k[i+1]-k[i],k[i]+p-k[i+1]+1))
                # print(c)
                continue
            if(k[i]+p-k[i+1]<n-1-k[i+1]+k[i]):
                
                t=n-1
                r=0
                # while(k[i]+p>=t):
                #     k[i]-=1
                #     r+=1
                r=k[i]-(n-2-p)
                # print(".",r)
                c.append(min(k[i+1]-k[i],r+n-1-k[i+1]))
                continue
                # print(".",c)
            
            c.append(k[i+1]-k[i])
    if(c==[]):
        print(0)
        continue 
    # print(c)
    print(min(c))