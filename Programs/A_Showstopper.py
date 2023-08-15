for aa in range(int(input())):
    n=int(input())
    # n,k,d,w=(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(a[n-1]==max(a) and b[n-1]==max(b)):
        print("YES")
        continue
    a.reverse()
    b.reverse()
    for i in range(n):
        if(a[0]==a[i]):
            b[i],a[i]=a[i],b[i]
    for i in range(n):
        if( )
