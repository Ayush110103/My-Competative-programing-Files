# cook your dish here
import sys
input = lambda: sys.stdin.readline().rstrip()

import bisect

def lower_bound(array, n):
    index = bisect.bisect_left(array, n)
    return index

for aa in range(int(input())):
    # n=int(input())
    n,q=map(int,input().split())
    li=list(map(int,input().split()))
    f=[]
    t=0
    for i in range(n-2):
        t+=((n-1-i)*(n-2-i))//2
        f.append(t)
    # print(f)
        
    li.sort()
    for i in range(q):
        k=int(input())
        r=lower_bound(f,k)
        print(li[r])
        
        



            

        
        