import math
for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    z=0
    for i in range(n-1):
        if(li[i]!=li[i+1]):
                z=1
                break
        
    if(z==0):
        print(0)
        continue
    k=min(li)
    t=li.index(k)+1
    if(k==1):
         print(-1)
         continue
    p=[]
    c=0
    gg=0
    ff=0
    while (c<30*n):
        c+=1
        e=0
        for i in range(n):
            if(li[i]!=k):
                li[i]=int(math.ceil(li[i]/k))
                e=1
                break
        if(e==1):
            p.append([i+1,t])
            if(li[i]<k):
                    k=li[i]
                    t=i+1
        # print(k)
        z=0
        for i in range(n-1):
                if(li[i]!=li[i+1]):
                        z=1
                        break
                
        if(z==0):
                gg=1
                break
        
            

            
        # print(li)
    if(gg==1):
            print(c)
            for i in p:
                print(*i)
    