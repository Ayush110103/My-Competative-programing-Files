for aa in range(int(input())):
    n=int(input())
    if(n==1):
        print("YES")
        print(1)
        continue
    if(n==3):
        print("NO")
        continue
    li=[]
    if(n%2==0):
        for i in range(n//2):
            li.append(-1)
            li.append(1)
        
        print("YES")
        print(*li)
    else:
        k=n//2
        for i in range((n//2)):
            li.append(-1*(k-1))
            li.append(k)
        li.append(-1*(k-1))
        print("YES")
        print(*li)

