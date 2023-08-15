import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200001)
h=[]
p=999999999
c=0
def dfs(node,visited,d,n,c):
    if(node==n):
        p=min(p,c)
        c=0
        return p
    if(visited[node]==True):
        c=0
        return c
    # c+=1,c
    visited[node]=True
    for i in d[node]:
        y=dfs(i,visited,d,n,c+1)
    return y

# n=int(input())
n,m=map(int,input().split())
d={}
k=[1]
for i in range(n):
    d[i+1]=[]
for i in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
# print(d)
ans=0
c=0
visited=[False]*(n+1)
t=dfs(1,visited,d,n,c)
print(t)



    
    
