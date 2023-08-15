for aa in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    cold=list(map(int,input().split()))
    hot=list(map(int,input().split()))
    aa=cold[li[0]-1]
    x=li[0]
    d={}
    for i in li:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    y=0
    d[li[0]]-=1
    for i in range(1,n):
        print(aa)
        if(x==li[i]):
            aa+=hot[li[i]-1]
            d[li[i]]-=1
            continue
        if(y==li[i]):
            aa+=hot[li[i]-1]
            d[li[i]]-=1
            continue
        if(y==0):
            y=li[i]
            aa+=cold[li[i]-1]
            d[y]-=1
            continue
        if(d[x]==0):
            x=li[i]
            aa+=cold[x-1]
            continue
        if(d[y]==0):
            y=li[i]
            aa+=cold[y-1]
            continue
        if(cold[x-1]-hot[x-1]>=cold[y-1]-hot[y-1]):
            y=li[i]
            aa+=cold[y-1]
            continue
        else:
            x=li[i]
            aa+=cold[x-1]
            continue
        
    print(aa)


        





        


        
             


