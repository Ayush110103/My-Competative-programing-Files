import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())
    # li=list(map(int,input().split()))
    k=min(n,m)
    m=max(m,n)
    if(k==1 and m>2):
        print(2)
        continue
    if(k==1 and m==2):
        print(3)
        continue
    if(k==1 and m==1):
        print(2)
        continue
    print(1)
      
    