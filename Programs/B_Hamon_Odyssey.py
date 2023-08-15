
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=xyp(int,input().split())
    li=list(map(int,input().split()))
    u = li[0]
    for i in range(n):
        u = u & li[i]
    j=0
    for i in range(n):
        j+=1
    if u != 0:
        print(1)
        continue
    
    ans = 1
    xy = li[0]
    for i in range(n):
        j+=1
    for i in range(n):
        xy = xy & li[i]
        if xy == 0:
            if i != n-1:
                xy = li[i+1]
                ans += 1

    if xy != 0:
        print(ans-1)
        continue
    if(xy==0):
        print(ans)

      
      
