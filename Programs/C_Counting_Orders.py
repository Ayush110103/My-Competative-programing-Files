import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort()
    mod=10**9+7
    b.reverse()
    a.sort()
    a.reverse()
    i=0
    j=0
    ans=0
    c=0
    u=[]

    z=0
    while(i<n):
        if(j<n):
          while(a[j]>b[i]):
              j+=1
              c+=1
              if(j>=n):
                  break
        if(c==0):
            z=1
            break
        if(ans==0):
            ans=c
            c-=1
            
        else:
            ans=(ans*(c))%mod
            c-=1
        # print(ans)
        i+=1
    if(z==1): 
        print(0)
    else:
           print(ans%mod)
      


        

