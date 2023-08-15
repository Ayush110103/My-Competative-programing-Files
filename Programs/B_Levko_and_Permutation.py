import math
n,k=map(int,input().split())
if(n==1 and k>0):
    print(-1)
    quit()
if(n==1 and k==0):
    print(1)
    quit()
if(n==k):
    print(-1)
    quit()
li=[]
for i in range(n):
    li.append(i+1)
if(n-1==k):
   print(*li)
   quit()
if(k==n-2):
    t=li[0]
    li[0]=li[n-1]
    li[n-1]=t
    print(*li)
    quit()
li=[1]
for i in range(k):
    li.append(i+2)

for i in range(k+1,n-1):
    li.append(i+2)
li.append(k+2)
t=li[0]
li[0]=li[len(li)-1]
li[len(li)-1]=t

print(*li)
    