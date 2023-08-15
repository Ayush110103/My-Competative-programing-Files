'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

for aa in range(int(input())):
    n,q=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort();
    d={}
    k=[]
    for i in range(n):
        k.append(0)
    t=k.copy()
    x=[]
    for i in range(q):
        a,b=map(int,input().split())
        a-=1;
        b-=1;
        x.append([a,b])
        
        k[a]+=1
        if(b+1<n):
           k[b+1]-=1
    for i in range(1,n):
        k[i]=k[i]+k[i-1]
    for i in range(n):
        if(k[i]in d):
            d[k[i]].append(i)
        else:
            d[k[i]]=[i]
    f=[]
    for i in d:
        f.append(i)
    f.sort()
    # print(d)
    c=0
    for i in f:
        while(len(d[i])>0):
            t[d[i][len(d[i])-1]]=li[c]
            d[i].pop()
            c+=1;
    # print(t)
    s=0
    p=[]
    for i in range(n):
        s+=t[i]
        p.append(s)
    a=0
    for i in range(q):
        if(x[i][0]==0):
            a+=p[x[i][1]]
            continue
        a+=p[x[i][1]]-p[x[i][0]-1]
    print(a)   
    print(*t)
        
        
        
           
        
        
        
