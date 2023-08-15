
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    if(len(li)==1):
        print(1)
        continue

    k=max(li[1:])
    i=li.index(k)
    print(i)
    if(i==n-1):
        k=[li[i]]+ li[:i]
        print(*k)
        continue
    else:
        x=0
        if(i-x-1>0):
          while True:
              if(li[i-x-1]<li[0]):
                
                if(i-x-2<0):
                   break
                x-=1
                continue
              if(li[i-x-1]>li[0]):
                  break
              
        t=li[i-x-1:i]
        print(t)
        t.reverse()

        k=li[i:]+t+li[:i-1-x]
        print(*li)


