import math
for aa in range(int(input())):
    n,k,d,w=(map(int,input().split()))
    li=list(map(int,input().split()))
    r={}
    for i in li:
        if(i in r):
            r[i]+=1
        else:
            r[i]=1
    c=1
    i=1
    z=0
    kk=k
    dd=d
    ww=w
    j=0
    ct=0
    g=li[0]
    while(i<n):
        print(c)
        if(kk==0 ):
            c+=1
            kk=k-1
            i+=1
            g=li[i-1]

            continue

        if(li[i]-g>d):
            kk=k-1
            c+=1
            i+=1
            g=li[i-1]
            continue
            
        
        if(li[i]-li[i-1]==0):
            if(r[li[i]]-1<=kk):
                kk=0
                
                i+=r[li[i]]-1
                continue
            
            c+=math.ceil((r[li[i]]-1-kk)%k)
            kk=k-(r[li[i]]-1-kk)%k
            
            i+=r[li[i]]-1
            g=li[i-(r[li[i]]-1-kk)%k]
            continue
        kk-=1
        i+=1
        dd-=1


    print(c)  
          

            
            

    