for i in range(int(input())):    
    n=int(input())
    li=list(map(int,input().split()))
    if(1 in li):
        print("YES")
        continue
    z=0
    for i in range(n):
        if(li[i]==i+1):
            z=1
            break
        if(li[i]<=i+1):
            z=1
            break

    if(z==1):
        print("YES")      
        continue
    print("NO")
    