for i in range(int(input())):    
    n,k=map(int,input().split())
    if((n-k)%2==0 and n-k>=0) or ((n-2*k)%2==0 and (n-2*k)>=0):
        print("YES")
        continue
    
    if(n%2==0):
        print("YES")
        continue
    print("NO")
            
    