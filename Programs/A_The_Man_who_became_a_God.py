
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    y=[]
    for i in range(n-1):
        y.append(abs(li[i]-li[i+1]))
    f=y.copy()
    y.sort()
    y.reverse()
    y=y[:k-1]
    print(sum(f)-sum(y))
    
        
        
    
        