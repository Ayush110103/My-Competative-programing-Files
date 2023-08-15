
for i in range(int(input())):
    n=int(input())
    ans=[]
    a=0
    ar=[]
    for i in range(1,n):
        ar.append(i)
    d={}
    for i in ar:
        d[i]=1
    d[1]=3
    k=[]
    b=n**2+1
    for i in range(b//2):
        a+=1
        b-=1
        d[1]=4
        if(a==b):
            k.append(a)
            
            
        else:    
            k.append(a)
            k.append(b)
            
     
    bt=0
    kk=1
    for i in range(n):
        m=[]

        for i in range(n):
            m.append(k[bt])
            bt+=1
       
        if(kk%2==1):
            print(*m)
        else:
            m.reverse()
            print(*m)   
        kk+=1 
         
    
 
