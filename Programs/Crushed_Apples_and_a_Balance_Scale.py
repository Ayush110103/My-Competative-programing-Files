import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())
    # li=list(map(int,input().split()))
    if(n==m):
        print("YES")
        continue
    if n%2!=0:
        print("NO")
        continue
    if(n<m):
        print("NO")
        continue
    c=0
    while(n%2==0):
        n=n//2
        c+=1
    # print(c)
    if(m%n==0):
        print("YES")
        continue
    else:
        print("NO")
        continue
    
    

    
        



        