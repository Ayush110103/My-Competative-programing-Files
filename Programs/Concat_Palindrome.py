
for aa in range(int(input())):
    n,m=map(int,input().split())
    a=list(input())
    b=list(input())
    f='abcdefghijklmnopqrstuvwxyz'
    if n<m:
        n,m=m,n
        a,b=b,a
    if n>=m:

       

        k={}
        for i in f:
            k[i]=0
        for i in b:
            k[i]+=1
        
        d={}
        for i in f:
            d[i]=0
        for i in a:
            d[i]+=1
        z=0
        for i in k:
            if d[i]>=k[i]:
                d[i]-=k[i]
            else:
                print( 'NO')
                z=1
                break
             
        if(z==1):
            continue
        x=[]
        for i in d:
            x.append(i)


        ss=0
        for i in x:
            if d[i]%2!=0:
                ss+=1
        v=(n+m)
        if v%2==1:
            if ss<=1:
                print('YES')
                continue
            else:
                print('NO')
                continue
    
        else:
            
            if ss==0:
                print( 'YES')
                continue
            else:
                print( 'NO')
                continue
    