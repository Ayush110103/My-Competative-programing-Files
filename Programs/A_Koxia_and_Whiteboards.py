for aa in range(int(input())):
    n,m=map(int,input().split())
    
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    for i in range(m):
       
        a[0]=b[i]
        a.sort()
    
    print(sum(a))

