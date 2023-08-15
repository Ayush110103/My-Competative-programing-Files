import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    z=0
    for i in range(1,n-1):
        for j in range(i):
          for k in range(i+1,n):
            if(li[i]-li[j]==li[k]-li[i]):
                z=1 
                break
          if(z==1):
             break
        if(z==1):
            break
    if(z==1):
        print("No")
    else:
        print("Yes")
          

             