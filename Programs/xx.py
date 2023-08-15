import sys
input = lambda: sys.stdin.readline().rstrip()
import math
for aa in range(int(input())):
    # n=int(input())
    x,y,r=map(int,input().split())
    # li=list(map(int,input().split()))
    print(math.ceil((x+(r//30))/y))
    