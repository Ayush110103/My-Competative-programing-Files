n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n-1):
    if(l[i+1]<l[i]):
        c+=abs(l[i+1]-l[i])
        l[i+1]=l[i]
print(c)
