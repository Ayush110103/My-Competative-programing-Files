import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m,h=map(int,input().split())
    c=list(map(int,input().split()))
    p=list(map(int,input().split()))
    c.sort()
    p.sort()
    c.reverse()
    p.reverse()
    ans=0
    for i in range(min(n,m)):
        ans+=min(c[i],p[i]*h)
    print(ans)
        
        
