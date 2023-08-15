import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
d={}
li=[]
for i in range(n):
    x,y=map(int,input().split())
    d[x]=1
    d[y]=-1 
    li.append(x)
    li.append(y)
    
    
li.sort()
# print(li)
c=0
m=0
for i in li:
    c+=d[i]
    m=max(m,c)
print(m)


