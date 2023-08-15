n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d={}
for i in b:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
x=[]
for i in d:
    x.append(i)
x.sort()
a.sort()
v=[]
for i in range(n):
    v.append(0)
for i in range(n):
    if(a[i] in x):
        if(v[i]==0):
            v[i]=1
            d[a[i]]-=1

y=[]
s=[]
for i in range(n):
    if(v[i]==0):
        y.append(a[i])
for i in range(len(x)):
    if(d[x[i]]!=0):

        s.append(x[i])
# print(s,y)
for i in range(len(y)):

    for j in range(len(s)):
        if(d[s[j]]>0):
            
            if(s[j]>y[i]):
                v[i]=1
                d[s[j]]-=1
                break
             



c=0
for i in v:
    if(i==0):
        c+=1
print(c)          

        




 