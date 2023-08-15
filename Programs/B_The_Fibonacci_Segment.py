def find(li,n):
    if(len(li)==1):
        return 1
    if(len(li)==2):
        return 2
    c=2
    
    max=0
    for i in range(2,n):
        a=li[i-2]
        b=li[i-1]
        if(a+b==li[i]):
            c+=1
            # a=li[i-1]
            # b=li[i]


        else:
            if(max<c):
                max=c
            c=2
    if(c>max):
        max=c
    return max






n=int(input())
a=list(map(int,input().split()))
print(find(a,n))

