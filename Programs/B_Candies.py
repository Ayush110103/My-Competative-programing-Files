for i in range(int(input())):    
    n=int(input())
    if(n==1):
        print(1)
        print(1)
        continue
    if(n%2==0):
        print(-1)
        continue
    c=0
    x=1
    li=[]
    while(n>3):
        # print(n)
        if((n//2)%2==0):
            n=(n//2)+1
            li.append(1)
        else:
            n=n//2
            li.append(2)
    li.append(2)
    li.reverse()
    print(len(li))
    print(*li)