for aa in range(int(input())):
    n,x,p=(map(int,input().split()))
    li=[]
    f=0
    for i in  range(1,201):
        f+=i
        li.append(f)
    # print(li)
    e=n-x
    tt=e%n
    z=0
    y=min(200,p)
    for i in range(y):
        if(tt==(li[i]%n)):
            z=1
            break
    if(z==1):
        print("Yes")
    else:
        print("No")


        
    