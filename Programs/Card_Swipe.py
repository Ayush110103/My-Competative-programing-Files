import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    d={}
    k=0
    c=0
    for i in range(n):
        if(li[i] in d):
             d[li[i]]+=1
             if (d[li[i]]%2==0):
                 c-=1
             else:
                 c+=1
        else:
            d[li[i]]=1
            c+=1
        k=max(k,c)
    print(k)
        
        