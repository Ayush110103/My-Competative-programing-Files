for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    s=1
    x=[]
    for i in li:
      s*=i
      x.append(s)
    k=x[n-1]
    r=-1
    for i in range(n-1):
       if(k/x[i]==x[i]):
          r=i+1
          break
    # print(r,x)
    if(r==-1):
       print(-1)
       continue
    else:
       print(r)
    

       
   

