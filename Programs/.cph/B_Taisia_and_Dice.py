
 

for aa in range(int(input())):
    # n=int(input())
    n,s,r=list(map(int,input().split()))
    k=s-r
    c=0
    li=[k]
    if(n==2):
        li.append(r)
        print(*li)
        continue
    u=[]
    for i in range(n-1):
        u.append(1)

    while(sum(u)!=r):
        z=0
        for i in range(n-1):
            u[i]+=1
            if(sum(u)==r):
                z=1
                break

        if(z==1):
            break
    u.append(k)
    print(*u)


    
