# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(d,v,c,node,g):
    
    if(v[node]==1):
        return g[node]
    v[node]=1
    
    if(d[node]==[] and node not in g):
        g[node]=c[node-1]
        return g[node]
    # if(d[node]==[] and node in g):
    #     g[node]=min(g[node],c[node-1])
    #     return g[node]
    g[node]=0
    for i in d[node]:
        g[node]+=dfs(d,v,c,i,g)
    g[node]=min(g[node],c[node-1])
    return g[node]
for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())
    c=list(map(int,input().split()))
    p=list(map(int,input().split()))
    # print(p)
    v=[0]*(n+1)
    g={}
    
    for i in range(m): 
        g[p[i]]=0
        v[p[i]]=1
        c[p[i]-1]=0
    d={}
    a=[]
    y=[]
    f=[]
    for i in range(n):
        x=list(map(int,input().split()))
        f.append(x[0])
        x=x[1:]
        d[i+1]=x
    # print(d)
    # print(v)
    # print(g)
    for i in range(1,n+1):
        if(v[i]==0): 
            op=dfs(d,v,c,i,g)
    g = dict(sorted(g.items()))
    # print(g)
    for i in g:
        print(g[i],end=" ")
    print()
    g={}
    
            
    


   

  

