for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    z=0
    s=li[0]
    d={}
    for i in li:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    if(len(d)==1):
        print("NO")
        continue
    li.sort()
    li.reverse()
    t=li[n-1]
    li.pop(n-1)
    li=[t]+li
    print("YES")
    print(*li)


