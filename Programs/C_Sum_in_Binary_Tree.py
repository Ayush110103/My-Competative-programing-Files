import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    k=0
    # li=list(map(int,input().split()))
    while(n!=1):
        k+=n
        n=n//2
    print(k+1)
