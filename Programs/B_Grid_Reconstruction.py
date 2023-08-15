for aa in range(int(input())):
    n=int(input())
    # l=(map(int,input().split()))
    li=[]
    k=[]
    if(n==2):
        print(3,2)
        print(1,4)
        continue
    if((n//2)%2==0):
        li=[n]
        for i in range(n//2-1):
            k.append(i+1)
            k.append(n-1-i)
        li=li+k
        li.append(n//2)
        
            
        # print(*li)
        k.append(n//2)

        k.append(n)
        for i in range(n):
            li[i]=li[i]*2
            k[i]=k[i]*2-1
        print(*li)
        print(*k)
    else:
        li=[n//2]
        for i in range(n//2-1):
            k.append(n-1-i)
            k.append(i+1)
        li=li+k
        li.append(n)
        # print(*li)
        k=[n,n//2]+k
        for i in range(n):
            li[i]=li[i]*2
            k[i]=k[i]*2-1
        print(*k)
        print(*li)
        
            
            

            


      
        