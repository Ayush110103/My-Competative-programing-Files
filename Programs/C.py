import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    u=[b[0]]*n
    v=[a[0]]*n
    if(u==b and v==a):
        print("YES")
        continue
    k=b.copy()
    y=[0]*n
    if(y==a or y==b):
        print("YES")
        continue

    k.reverse()
    if(a==b or (a==k and n%2!=0)):
        print("YES")
        continue
    if(a==k and n%2==0):
        print("NO")
        continue
    c=[]
    for i in range(n):
        c.append(abs(a[i]-b[i]))
    if(c==y):
        print("YES")
        continue
        
    if(c==a or c==b):
        print("YES")
        continue
    p=c.copy()
    p.reverse()
    if(p==b and n%2!=0):
        print("YES")
        continue
    if(p==b and n%2==0):
        print("NO")
        continue
    
    f=0
    for i in range(n):
        if(c[i]!=0):
          if(b[i]%c[i]==0):
              continue
          else:
              f=1
              break
        
    if(f==0):
        print("YES")
        continue
    print("NO")


        
    

        
    
