import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200001)
def dfs(node,visited,d):
    if visited[node]:
        return
    visited[node]=True
    for i in d[node]:
        dfs(i,visited ,d)
    


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
visited=[False]*(n+1)
dfs(1,visited,d)

# here
for i in range(1,n+1):
    if not visited[i]:
        k.append(i)
        dfs(i,visited ,d)
        ans+=1
print(ans)

for i in range(len(k)-1):
    print(k[i],k[i+1])

    
    
