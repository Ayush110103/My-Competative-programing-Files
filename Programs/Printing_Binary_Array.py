import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    a=[]
    for i in range(n):
        if(li[i]==0):
            a.append(1)
        else:
            a.append(0)
    print(*a)

    
        


    
    