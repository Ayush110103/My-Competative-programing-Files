for aa in range(int(input())):
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    d={}
    for i in range(n):
        d[i]=n-i
    d[n]=1
    li.sort()
    c=0
    i=0
    f=0
    for i in range(n):
        if(m-li[i]>=0):

            c+=1
            # if(li[i]==0):
            #     f+=1
            m-=li[i]
    # if(f>0):

    #      print(d[c]+f)
    # else:
    #     print(d[c]+1)
    if(c==n or c==n-1):
        # print("N")
        print(1)
        continue
    if(c==0):
        # print("T")
        print(n+1)
        continue
   
    if(m==0 and 0 in li):
       print(n-c+1)
       continue
    print(n-c)

    
    
    