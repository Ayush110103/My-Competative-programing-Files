import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    li.reverse()
    u=0
    u=n-li[0]
    c=0
    for i in range(1,m):
        if(u>=li[i]):
            u=n
        else:
            u=n-(li[i]-u)
        if(u==n):
            break
    print(n-u)
          
          
          
                