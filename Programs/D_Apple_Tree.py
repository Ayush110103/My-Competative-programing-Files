import sys
from collections import deque

def isval(mid):
    if ((mid-1)*mid)//2 < m:
        return False
    return True

def dfs(x, jad=-1):
    if len(g[x]) == 1 and x != 1:
        vertex[x] = 1
    for v in g[x]:
        if v != jad:
            dfs(v, x)
            vertex[x] += vertex[v]

# Input and Output
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n+1)]
    vertex = [0] * (n+1)
    for _ in range(n-1):
        l, r = map(int, input().split())
        g[l].append(r)
        g[r].append(l)

    dfs(1)

    m = int(input())
    for _ in range(m):
        l, r = map(int, input().split())
        print(str(vertex[l]*vertex[r]) + '\n')
