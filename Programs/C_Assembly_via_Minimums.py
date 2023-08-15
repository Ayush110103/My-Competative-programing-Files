for i in range(int(input())) :
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    d = {}
    for i in li :
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    #print(d)
    ans = []
    op = n-1
    for i in d :
        k = 0
        j=0
        while(j<200000):
        
            k+=op
            op-=1
            ans.append(i)
            if k==d[i]:
                break
            j+=1
    ans.append(ans[len(ans)-1])

    print(*ans)