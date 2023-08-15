import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    if(sum (a)==sum(b)):
        print("Draw")
        continue
    if(sum(a)>sum(b)):
        print("Tsondu")
        continue
    print("Tenzing")
        
        
