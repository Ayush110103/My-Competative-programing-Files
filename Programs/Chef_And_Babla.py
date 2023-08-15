for aa in range(int(input())):
    k=int(input())
    li=list(map(int,input().split()))
    p=[]
    n=[]
    for i in range(k):
        if(li[i]<0):
            n.append(li[i])
        else:
            p.append(li[i])
    if(p==[]):
        print(abs(max(n))-1)
        continue
    if(n==[]):
        print(min(p)-1)
        continue
    if(0 in li):
        print(-1)
        continue
    print(min(abs(max(n))-1,min(p)-1))


    