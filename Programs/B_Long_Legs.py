import math
for i in range(int(input())):    
    a,b=map(int,input().split())
    x=min(a,b)
    y=max(a,b)
    r=1
    g=1
    t=math.gcd(x,y) 
    for i in range(2,min(x//2,10000)+1):
        if(x%i==0):
            r=i
            break
    for i in range(2,min(y//2,100000)+1):
        if(y%i==0):
            g=i
            break 
    c=0 
    
    # print(t)
    # c+=t-1+x//t
    # print(r,g)
    w=t
    for i in range(2,min(y//2,100000)+1):
        if(t%i==0):
            w=i
            break 
    # print(w)
    q=1000000
    for i in range(1,1000):
        q=min(q,(x%i+(x-x%i)//i)+(y%i+(y-y%i)//i)+i-1)
    if(t==1):
        if(r==1 and g==1):
            c=q
            
        elif(r<=g ):
            c+=(x%g+(x-x%g)//g)+y//g+g-1
        else:
            # print(r)
            c+=y%r+(y-y%r)//r+r-1+x//r
        # c+=y//g+g-1
    else:
        
        c+=w-1+x//w
        # print(c,"a")
        # print(w,"a")
        c+=y//w
    print(c)
  


        
    
    