for kk in range(int(input())):
    # n=int(input())
    li=list(map(int,input().split()))
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k=int(input())
  
    d={}
    for i in range(26):
        d[s[i]]=li[i]
    # print(d)
    o=[]
    z=0
    for i in range(k):
        w=input()
        t=""
        for j in range(len(w)):
            t+=str(d[w[j]])
        
        o.append(t)
    # print(o)
    if(len(set(o))==k):
        print("Case #"+str(kk+1)+": NO")
    else:
        print("Case #"+str(kk+1)+": YES")
      


        