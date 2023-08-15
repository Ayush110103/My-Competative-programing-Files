for aa in range(int(input())):
    n,k=map(int,input().split())
    li=[]
    # a=list(map(int,input().split()))
    # b=list(map(int,input().split()))
    f=n-k+1
    
    for i in range(n):
        li.append(i+1)
    if(f==1 or f==n):
        print(*li)
        continue
    x=[]
    for i in range(n//2):
        
        
        x.append(n-i)
        x.append(i+1)
    if(n%2!=0):
        x.append((n//2)+1)
    print(*x)
    
