n=int(input())
x=[]
y=[]
for i in range(n):
    sub=list(map(int,input().split()))
    x.append(sub[0])
    y.append(sub[1])
h=[]
o=[]
for i in range(n):
    h.append(n-1)
    o.append(n-1)
d={}
for i in range(n): 
    d[y[i]]=0
for i in range(n): 
    if(x[i] in d):
      d[x[i]]+=1
for i in range(n):
     h[i]+=d[y[i]]
     o[i]-=d[y[i]]
     print(h[i],o[i])

