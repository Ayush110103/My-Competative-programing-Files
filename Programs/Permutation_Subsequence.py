for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    lst=li.copy()
    lst.sort()

    d={}
    for i in range(n):
        if(li[i] in d):
            d[li[i]]+=1
        else:
            d[li[i]]=1
    # print()
    # x=[]
    # for i in d:
    #     x.append(i)
    # x.sort()
    sum=0
    k=1
    p=1
    while True:
        if(k>n):
             break
        if(k not in d ):
            break
        # sum+=d[k]*d[k]
        k+=1
    # print(k)
    
    # print(sum

    for i in range(1,k):
            p=p*d[i]
            sum+=p
                    
    print(sum%1000000007)
   

