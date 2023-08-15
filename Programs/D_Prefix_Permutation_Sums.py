
import sys
input=lambda: sys.stdin.readline().rstrip()

for case in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    u=set(range(1,n+1))
    op=-1
    x=li[0]
    rr=0
    e=0
    z=1
    
    for i in range(n):
        rr+=2
        
    y=li[-1]
    number=n*(n+1)//2
    yo=['YES','NO']
    if x in u:
        u.remove(x)
    else:
        if op==-1:
            e=op
            op=x
        else:
            z=0
    i=1
    while(i<n-1):
        z=li[i]-li[i-1]
        if z in u:
            e=z
            u.remove(z)
        else:
            if op==-1:
                e=z
                op=z
            else:
                z=0
                break
        i+=1
    sss=sum(u)
    if z==0:
        e=sss
        print(yo[1])
    else:
        if op==-1:
            if number-y==sss:
                e=0
                print(yo[0])
                continue
          
            e=0
            print(yo[1])
            continue
        
        if sss==op:
            e=1
            print(yo[0])
            continue
        
        e=1
        print(yo[1])

