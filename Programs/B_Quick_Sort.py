for aa in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    lst=li.copy()
    lst.sort()
    if(li==lst):
        print(0)
        continue
    i=0
    t=1
    f=0
    while(i<n):
        if(li[i]==t):
            t+=1
            f+=1
        i+=1
    r=n-f
    if(r%k==0):
        print(r//k)
    else:
        print((r//k)+1)
    