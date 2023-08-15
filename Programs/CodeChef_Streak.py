import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    k=list(map(int,input().split()))
    a=0
    b=0
    z=0
    c=0
    for i in range(n):
        if(li[i]==0):
            a=max(a,c)
            c=0
        else:
            c+=1
    a=max(a,c)
    c=0
    for i in range(n):
        if(k[i]==0):
            b=max(b,c)
            c=0
        else:
            c+=1
    b=max(b,c)
    c=0
    if(a>b):
        print("Om")
        continue
    if(a==b):
        print("Draw")
        continue
    print("Addy")