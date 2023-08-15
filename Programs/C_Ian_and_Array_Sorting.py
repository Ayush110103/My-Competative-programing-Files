for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    
    l=li.copy()
    l.sort()
    if(l==li):
        print("YES")
        continue
    l.reverse()
    if(l==li and li!=[2,1]):
        print("YES")
        continue
    if(li==[2,1]):
        print("NO")
        continue
    z=-1
    k=li[1]-li[0]
    if(k>0):
        z=1
    if(k<0):
        z=2
    if(k==0):
        z=3
    c=0
    for i in range(1,n-1):
        t=li[i+1]-li[i]
        if(t>0):
            if(z==1):
                continue
            elif(z==2):
                c+=1
                z=1
                
            elif(z==3):
                z=1
                continue
        elif(t<0):
            if(z==2):
                continue
            elif(z==1):
                c+=1
                z=2
            elif(z==3):
                z=2
                continue
        elif(t==0):
            if(z==3):
                continue
            else:
                
                z=3
        if(c>1):
            break
    if(c>1):
        print("NO")
        continue
    print("YES")
  