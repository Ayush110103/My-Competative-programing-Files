

for aa in range(int(input())):
    # n=int(input())
    n,m,k,h=map(int,input().split())
    li=list(map(int,input().split()))
    c=0
    for i in li:
        f=abs(i-h)
        
        if(f%k==0):
            umb=f//k
            if(umb==0):
                continue
            if(umb<m):
                c+=1
    print(c)