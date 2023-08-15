
for aa in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    z=0
    for i in range(n//2):
        if(li[i]==li[n-i-1]):
            pass
        else:
            z=1
    if(z==0):
        print("YES")
        continue
    t=0
    for i in range(n//2):
        t+=abs(li[i]-li[n-i-1])
    if(t%k==0):
        print("YES")
    else:
        if((t%k)%2==1):
            if(n%2!=0):
                print("YES")
                continue
            else:
                print("NO")
                continue
        if(t%k)%2==0:
            print("YES")
            continue
        
        print("NO")

    
        

