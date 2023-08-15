# cook your dish here
# cook your dish here
# cook your dish here
for aa in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    if(n%2!=0):
        print("NO")
        continue
    # print(d)
    z=0
    for i in d:
        if(d[i]%2!=0):
            z=1
            break
        
    if(z==0):
        print("YES")
    else:
        print("NO")