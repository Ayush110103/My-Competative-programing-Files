import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    if(n<=2):
        print(0)
        continue
    
        
    d={}
    for i in range(n):
        if(li[i] in d):
            d[li[i]].append(i+1)
        else:
            d[li[i]]=[i+1]
    p=[]
    # print(d)
    for i in d:
        d[i].append(n+1)
        x=[d[i][0]-1]
        u=0
        for j in range(1,len(d[i])):
            x.append(abs(d[i][j]-d[i][j-1]-1))
        h=max(x)//2
        x.remove(max(x))
        x.append(h)
        p.append(max(x))
    # print(p)
    print(min(p))
                


  
    

            
            