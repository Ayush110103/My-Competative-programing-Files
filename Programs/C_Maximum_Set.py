for aa in range(int(input())):
    l,r=map(int,input().split())
    k=r
    c=0
    while(k<=l):
          c+=1
          k=k*2
    x=2**(c-1)
    li=[]
    for i in range(r,l+1):
         if(x*i)<=l:
              li.append(i)
    
         
    