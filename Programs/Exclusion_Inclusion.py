import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    f=sum(li)
    p=[]
    s=0
    for i in range(n):
        s+=li[i]
        p.append(s)
    ans=[f]
    for i in range(n-1):
        ans.append(f-p[i])
    print(*ans)
        
        
        