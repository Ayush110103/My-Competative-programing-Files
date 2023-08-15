no=int(input())
x=[]
n=[]
p=[]
for i in range(no):
    x.append(int(input()))
for i in x:
    if(i<0):
        n.append(abs(i))
    if(i>0):
        p.append(i)
    if(i==0):
        p.append(0)
        n.append(0)

if(sum(p)>sum(n)):
    print("first")
if(sum(n)>sum(p)):
    print("second")
if(sum(p)==sum(n)):
    z=0
    for i in range(min(len(p),len(n))):
        if(p[i]==n[i]):
            continue
        if(p[i]>n[i]):
            z=1
            print("first")
            break
        if(p[i]<n[i]):
            z=1
            print("second")
            break
    if(z==1):
        quit()
    else:
        if(len(p)>len(n)):
                print("first")
        if(len(p)<len(n)):
                print("second")
        if(len(p)==len(n)):
                if(x[no-1]<0):
                    print("second")
                else:
                    print("first")

