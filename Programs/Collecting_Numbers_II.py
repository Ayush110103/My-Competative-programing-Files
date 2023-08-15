import sys
input = lambda: sys.stdin.readline().rstrip()


n,m=map(int,input().split())
li=list(map(int,input().split()))
c=0
d={}
for i in range(n):
    d[li[i]]=i


for i in range(n-1):
    if(d[i+2]-d[i+1]<0):
    
        c+=1
g=0
for i in range(m):
    x,y=map(int,input().split())
    x=x-1
    y=y-1
    if(li[x]>li[y]):
        c-=1
    
        t=li[x]
        li[x]=li[y]
        li[y]=t
        
    



        
    
    