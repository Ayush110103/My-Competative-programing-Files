for i in range(int(input())):
    x,y=map(int,input().split())
    if(x==0 and y==0):
        print("YES")
        continue
    if(x==0 or y==0):
        print("NO")
        continue
        
    if(x==y and x%3==0):
        print("YES")
        continue
    m=max(x,y)
    n=min(x,y)
    if(int(m/n)==2):
        print("YES")
        continue
    u=m-n
    if(m-(2*u)==(n-u) and (n-u)%3==0):
        print("YES")
        continue 
        
    print("NO")