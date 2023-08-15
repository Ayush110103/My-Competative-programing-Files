
    # n=int(input())
n,m=(map(int,input().split()))
v=[]
for i in range(n+1):
    v.append(0)
t=[1,2,3]
for i in range(m):
    sub=list(map(int,input().split()))
    x=[]
    t=[1,2,3]
    if(v[sub[0]]+v[sub[1]]+v[sub[2]]==0):
        v[sub[0]]=1
        v[sub[1]]=2
        v[sub[2]]=3
        continue
    for j in sub:
        
        if(v[j]!=0):
            r=v[j]
    for j in sub:
        if(v[j]==0):
            if(t[0]==r):
                v[j]=t[1]
            
            if(t[1]==r):
                v[j]=t[0]
            if(t[2]==r):
                v[j]=t[0]
            y=v[j]
            break
    for j in sub:
        if(v[j]==0):
            v[j]=6-r-y
v.pop(0)
print(*v)
        

        
                
        
    
            

    
    