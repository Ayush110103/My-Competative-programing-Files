import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
d={}
a=[]
b=[]
f={}
for i in range(n):
    x,y=map(int,input().split())
    a.append([y,x])
a.sort()

# print(a) 
c=0
m=-1
i=0
while(i<n):
    if(a[i][1]>=m):
        m=a[i][0]
        c+=1
        i+=1
    else:
        i+=1
print(c)
    
