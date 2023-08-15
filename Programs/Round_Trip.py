

# def dfs(node, p,path,d,visited):
#     if(path[0]==node):
#         if(len(path)>=2):
#             return path
#         else:
#             return [-1]
    
   
#     if(visited[node]==True and node!=p):
#        path=[]
#        path.append(node)
#        return path
#     if(visited[node]==True):
#         return [-1]
#     visited[node]=True
#     for i in d[node]:
#         if(visited[i]==False):
#             path=dfs(i, node,path,d, visited)
#             if(len(path)>=2):
#                 path.append(i)
#                 return path
#     return path

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200001)
 
s=-1
e=-1

def dfs (node,parent,visited,d):
    visited[node]=True
    p[node]=parent
    for i in d[node]:
        if(i==parent):
            continue
        if(visited[i] ):
            global s,e
            e=i
            s=node
            return True
        if(visited[i]==False): 
            if(dfs(i,node,visited,d)):
                return True
    return False



    
    
        
n, m = map(int, input().split())
d = {}
for i in range(1, n + 1):
    d[i] = []
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
visited = [False] * (n + 1)
p=[0]*(n+1)
z=0
for start in range(1, n + 1):
    if(visited[start]!=True):
        if(dfs(start,-1,visited,d)):
            z=1
            break

if(z==0):
    print("IMPOSSIBLE")
    quit()
if(z==1):
    # print(e,s)
    t=[e]
    while(s!=e):
        t.append(s)
        s=p[s]
    t.append(e)
    print(len(t))
    print(*t)



    

        
        
     
  
  
 