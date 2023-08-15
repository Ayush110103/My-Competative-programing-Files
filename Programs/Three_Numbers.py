for aa in range(int(input())):
    li=list(map(int,input().split()))
    li.sort()
    a=li[0]
    b=li[1]
    c=li[2]
    d=0
    
    if abs(a-b)%2==0 and abs(b-c)%2==0 and (c-a)%2==0:
         pass
    else:
        print(-1)
        continue
    if((li[1]-li[0])%2!=0):
        print(-1)
        continue
    else:
        d=(li[1]-li[0])//2
        li[0]=li[1]=(li[0]+li[1])//2
        li[2]+=d
    if((li[2]-li[0])%2!=0):
        print(-1)
        continue
    else:
        # print(c)
        d+=(li[2]-li[0])//2
    # print(li)
    print(d)

    
    
    