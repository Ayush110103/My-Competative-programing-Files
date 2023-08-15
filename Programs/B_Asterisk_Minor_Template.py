
for aa in range(int(input())):
    
    a=input()
    b=input()
   
    n=len(a)
    z=0
    m=len(b)
    for i in range(n-1):
        g=a[i]+a[i+1]
        if(g in b):
            z=1
            break
    if(z==1):
        print("YES")
        print("*"+g+"*")
        continue
    z=0
    if(a[0]==b[0]):
        g=a[0]
        z=1

    if(z==1):
        
            print("YES")
            print("*"+g)
            continue
    if(a[n-1]==b[m-1]):

        g=a[n-1]
        print("YES")
        print(g+"*")
        continue
    
    print("NO")

                
 
               







