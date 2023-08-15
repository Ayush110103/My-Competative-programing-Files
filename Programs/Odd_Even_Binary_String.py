for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    
    c=0
    for i in li:
        if(i==0):
            c+=1
    if(c%2==0):
        print("YES")
    else:
        print("NO")
        

    