import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    
    n,m=map(int,input().split())
    if(n==m):
        print("YES")
        continue
    z=0
    for i in range(100000):
        if(n==m):
            z=1
            break
        if(n>m):
            n-=1
            m+=1
            continue
        if(n<m):
            n+=3
            m-=1
    if(z==1):
        print("YES")
        continue
    print("NO")      
        
    