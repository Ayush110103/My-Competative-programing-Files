n,m=map(int,input().split())
if(m==0):
    print("YES")
    quit()
a=list(map(int,input().split()))
a.sort()
z=[]

if(n in a or 1 in a):
    print("NO")
    quit()
if(m<=2):
    print("YES")
    quit()

for i in range(m-1):
    if(a[i+1]-a[i]>1):
        z.append(a[i]+1)
        z.append(a[i+1]-1) 


e=0
d=a[0]-1
# print(z)
if(z==[]):
    print("NO")
    quit()
z.append(a[m-1]+1)
z.append(a[m-1]+1)
for i in range(0,len(z),2):
    
    if(z[i]-d<=3):
        d=z[i+1]
        # print(d)


    else:
        e=1
        break

if(e==1):
    print("NO")

else:
    print("YES")

