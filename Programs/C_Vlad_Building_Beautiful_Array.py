import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li.reverse()
    s=-1
    t=-1
    y=0
    x=0
    p=[]
    q=[]
    for i in range(n):
        if(li[i]%2==0):
            x+=1
            p.append(li[i])
        else:
            y+=1
            q.append(li[i])
    

    if(y==0 or x==0):
        print("YES")
        continue
    p.sort()
    q.sort()
    k=min(li)
    
    if(max(p)-min(q)<0):
            print("NO")
            continue
    if(min(p)-min(q)<0):
         print("NO")
         continue
    
    print("YES")
            
        
    
        
