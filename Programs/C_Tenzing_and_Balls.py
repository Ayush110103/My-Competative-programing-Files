import sys
input = lambda: sys.stdin.readline().rstrip()

import bisect
def lower_bound(arr, x):
    index = bisect.bisect_left(arr, x)
    return index

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    # print(lower_bound([1,2,4,5,8],9))
    d={}
    for i in range(n):
        if(li[i] in d):
                d[li[i]].append(i)
        else:
            d[li[i]]=[i]
    d=sorted(d.items(), key=lambda x:x[1])
    # print(d)
    
    