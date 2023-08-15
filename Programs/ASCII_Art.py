import sys
input = lambda: sys.stdin.readline().rstrip()

 
import math
t = int(input())
for kk in range(t):
    
    n = int(input())
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d={}
    for i in range(26):
        d[s[i]]=i+1 
    if n <= 26:
        print("Case #{}: {}".format(kk+1, chr(64+n)))
    else:
        
        t=26*2
        n=n-26
        if(n<=t):
            n=int(math.ceil(n/2))
            print("Case #{}: {}".format(kk+1, chr(64+n)))
            continue
        z=0
        k=3
        while(n>t):
            n=n-t
            t=26*k
            if(n<=t):
                n=int(math.ceil(n/k))
                print("Case #{}: {}".format(kk+1, chr(64+n)))

                break
            k+=1
        
        




            
       