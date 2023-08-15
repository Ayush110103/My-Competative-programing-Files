import sys
input = lambda: sys.stdin.readline().rstrip()


for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    x,y=[],[]
    
    li=list(map(int,input().split()))
    if(n==1):
        print(li[0])
        continue
    for i in range(n):
        if(i%2==0):
            x.append(li[i])
        else:
            y.append(li[i])
    # print(x,y)
    a=0
    b=0
    for i in range(len(x)):
        if(x[i]>0):
            a+=x[i]
    
    for i in range(len(y)):
        if(y[i]>0):
            b+=y[i]
    
    if(max(a,b)==0):
        print(max(li))
        continue
    print(max(a,b))
    
            