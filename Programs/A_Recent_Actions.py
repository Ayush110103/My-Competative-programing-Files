for aa in range(int(input())):
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    
    k=[]
    for i in range(n):
        k.append(i+1)
    d={}
    for i in range(m):
        if li[i] not in d:
               d[li[i]]=i+1
    
    x=[]
    for i in d:
        if(len(x)<n):
           x.append(d[i])
    # print(x)
    if n>len(x):
      for i in range(n-len(d)):
          x.append(-1)
    x.reverse()
    print(*x)
         
         
         
        