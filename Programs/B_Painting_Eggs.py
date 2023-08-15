n=int(input())
a=[]
b=[]
for i in range(n):
    p,q=map(int,input().split())
    a.append(p)
    b.append(q)
s=""
x=0
y=0
z=0
for i in range(n):
    # print(s)
    if(x>=y):
        if(x-y+a[i]<=500):
            s+="A"
            x+=a[i]
            continue

        elif(x-y-b[i]<=500):
            s+="G"
            y+=b[i]
            continue
        z=1
        break
    else:
        if(y-x+b[i]<=500):
            s+="G"
            y+=b[i]
            continue

        elif(y-x-a[i]<=500):
            s+="A"
            x+=a[i]
            continue
        z=1
        break

if(z==0):
    print(s)       
else:
    print(-1)
    
    