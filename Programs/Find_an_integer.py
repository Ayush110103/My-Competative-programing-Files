# cook your dish here
for aa in range(int(input())):
    x,y=map(int,input().split())
    t=y%x
    k=x%y
    v=x-t
    if(t==0):
        v=0
    u=y-k
    if(k==0):
        u=0
    li=[]
    
    for i in range(1,500):
        t=x*i+v
        li.append(t)
    z=0
    for i in li:
        if(i%y==u):
            z=1
            break
    if(z==1):
       print(i)
    else:
        p=[]
        for i in range(500,1000):
            p.append(i)
        for i in p:
          if(i%y==u):
            z=1
            break  
        if(z==1):
            print(i)
            
        
    
    





