for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    # li=list(map(int,input().split()))
    li=[]
    for i in range(n):
        li.append(2*(i+1))
    print(*li)
        