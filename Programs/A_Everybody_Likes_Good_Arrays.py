for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    d={}
    c=0
    if(len(li)==1):
        print(0)
        continue

   
    

    for i in range(n-1):
        if(li[i]+li[i+1])%2==0:
            c+=1
        
    print(c)
        
    

    
        
    # print(n-c)
