for aa in range(int(input())):
    n=int(input())
    if(n%2!=0):
        print(-1)
        continue
    k=[]
    li=[1,2]

    # for i in range(3,n+1):
    #     k.append(i)
    # for i in range(3,n):
    #     j=0
    #     while(k[j]%i==0):
    #         j+=1
    #     li.append(k[j])
    #     k.pop(j)
        
    for i in range(3,n+1,2):
        li.append(i+1)
        li.append(i)

    # li.append(3)
   
    # li.append(k[0])
    print(*li)