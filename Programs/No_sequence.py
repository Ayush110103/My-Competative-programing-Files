# cook your dish here


for aa in range(int(input())):
    # n=int(input())
    n,k,s=(map(int,input().split()))
    li=[]
    x=[]
    for i in range(n):
        li.append(k**i)
    
    print(li)
    k=sum(li)
    if(k<s):
        print("-2")
    
    a=[]
    if(s in li):
        t=li.index(s)
        for i in range(n):
            if(i!=t):
              a.append(0)
            else:
                a.append(1)
        print(*a)
        continue
    if(k==s):
        for i in range(n):
            a.append(1)
        print(*a)
        continue
    for i in range(n):
        a.append(1)
        
    w=-1
    for i in range(n):
        if(s<li[i]):
            w=i
            break
    if(w==-1):
        w=n-1
    q=li[:w]
    if(s-li[w-1]<li[w]-s):
        if(sum(q)==s):
            for i in range(w,n):
                a[i]=0
            print(*a)
    else:
       
        t=li[w]-s




    


