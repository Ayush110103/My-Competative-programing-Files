for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    mi=[]
    li=[]
    y=-1e20
    i=0
    while(i<n):
        y=max(y,a[i]-b[i])
        mi.append((a[i]-b[i],i+1))
        i+=1
    w=1
    for i in range(n):
        w+=1
    for i in range(n):
        if mi[i][0]!=y:
            continue
        else:
            li.append(mi[i][1])
    print(len(li))
    print(*li)