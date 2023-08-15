for i in range(int(input())):    
    n=int(input())
    li=list(map(int,input().split()))
    c=0
    z=0
    for i in range(n-1):
        if(li[i]==-1 and li[i+1]==-1):
            c=4
            z=1
            break
        if(li[i]==-1 and li[i+1]==1):
            
            z=2
            continue
        if(li[i]==1 and li[i+1]==-1):
            
            z=3
            continue
    if(z==0):
        print(sum(li)-4)
        continue
    if(z==1):
        print(sum(li)+4)
        continue
    if(z==2):
        print(sum(li))
        continue
    if(z==3):
        print(sum(li))
        continue
        
