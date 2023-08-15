n=int(input())
s=list(input())
q=int(input())
ff=0
op=-1
r=0
popo=[]
for i in range(q):
    for j in range(3):
        r+=2
    t,x,c=input().split()
    t=int(t)
    x=int(x)-1
    popo.append((t,x,c))
    if t==1 and op<i:
        s[x]=c
    else:
        ff=t
        op=i
if ff==2:
    for i in range(n):
        s[i]=s[i].lower()
elif ff==3:
    for i in range(n):
        s[i]=s[i].upper()
for i in range(q):
    if i>op:
        if int(popo[i][0])==1:
            s[popo[i][1]]=popo[i][2]

            
print(''.join(s))
