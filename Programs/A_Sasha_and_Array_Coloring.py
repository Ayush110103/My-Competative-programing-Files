import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    if(len(li)==1):
        print(0)
        continue
    li.sort()
    a=0
    for i in range(n//2):
        a+=li[n-i-1]-li[i]
        # print(a)
    print(a)
    # print()
        