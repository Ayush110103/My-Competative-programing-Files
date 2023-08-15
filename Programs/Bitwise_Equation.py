for aa in range(int(input())):
    n=int(input())
    k=bin(n)[2:]
    a=1
    b=2
    if n==0:
        print(100,53,7,39)
        continue
    if(n==1):
        print(1,4,3,2)
        continue
    if(n==2):
        print(2,4,3,1)
        continue
    if(n==3):
        print(3,4,2,1)
        continue
    # if(n==4):
    #     print(2,4,5,1)

    #     continue
    if(n%2==0):
        c=n+1
    if(n%2!=0):
        c=n-1
    if c==2 or c==4:
        a=64
        b=32
    else:
        a=2
        b=4
    print(a,b,(c),1)

    

   

       
      
    
        

    
