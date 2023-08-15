
n=int(input())
x=[]
y=[]
for i in range(n):
    sub=list(map(int,input().split()))
    x.append(sub[0])
    y.append(sub[1])
d={}
for i in range(n):
    if x[i] in d:
        d[x[i]].append(i)
    else:
        d[x[i]]=[i]
x.sort()
f=[]
o=[]
for i in range(n):
    if(x[i] in o):
        continue
    o.append(x[i])


c=0

for i in o:
    
    if(len(d[i])>1):
        maxy=0
        for j in d[i]:
            if(y[j]>maxy):
                maxy=y[j]
        f.append(maxy)
    else:
        f.append(y[d[i][0]])
        
# t=[]
# # print(d,f)
# print(f)
# for i in f:
#     t=t+i
# print(y)
    
# print(t)
z=0
if(len(f)==1):
    print(max(y))
    quit()
for i in range(len(f)-1):
    if(f[i]<=f[i+1]):
        continue
    else:
        z=1
        break
if(z==1):print(max(x))
else:
    print(max(y))



    

