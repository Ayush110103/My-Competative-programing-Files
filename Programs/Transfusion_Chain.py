import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(input().split())
    a=li.count("A")
    b=li.count("B")
    c=li.count("AB")
    d=li.count ("O")
    print(max(a+d+c,b+c+d))


