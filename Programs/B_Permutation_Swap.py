import math
for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    k=-1
    for i in range(n):
        if(li[i]!=i+1):
            if(k==-1):
                k=abs(li[i]-(i+1))
                continue
            
            k=math.gcd(k,abs(li[i]-(i+1)))
    print(k)
        