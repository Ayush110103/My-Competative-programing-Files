import sys
input = lambda: sys.stdin.readline().rstrip()

def highestPowerof2(n):
 
    res = 0;
    for i in range(n, 0, -1):
         
        # If i is a power of 2
        if ((i & (i - 1)) == 0):
         
            res = i
            break
         
    return res

import math

for _ in range(int(input())):
    n,k=map(int,input().split())
    if int(math.log(n+1,2))>=k:
        print( 2**k)
    else:
        print(n+1)   
        


    

    