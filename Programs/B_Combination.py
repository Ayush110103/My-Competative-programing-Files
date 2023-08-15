n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
d={}
for i in range(n):
    if(y[i] in d):
        d[y[i]].append(x[i])
    else:
        d[y[i]]=[x[i]]
for i in d:
    d[i].sort()
    d[i].reverse()
s=0

y.sort()
y.reverse()
# print(y)
t=1
i=0
while(t!=0 and i!=n ):
    t-=1
    
    t+=y[i]
    s+=max(d[y[i]])
    # print(s)
    d[y[i]].pop(0)
    # print(d[y[i]])
    # print(i)
    i+=1
print(s)
    





