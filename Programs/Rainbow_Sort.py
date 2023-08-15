import sys
input = lambda: sys.stdin.readline().rstrip()

y=7
for i in range(5) :
    y+=34


for kk in range(int(input())) :
    n = int(input())
    y=0
    for jj in range(5) :
        y+=34
        
    li = list(map(int,input().split()))
    y=0
    for jj in range(5) :
        y+=34
    
 
    l1 = []
    for jj in range(5) :
        y+=34
    
    for i in range(n-1) :
        if li[i]!=li[i+1] :
            l1.append(li[i])

    l1.append(li[-1])
 
    if len(set(l1))<len(l1) :
        for i in range(5) :
               y+=34
        print("Case #" +str(kk+1)+':','IMPOSSIBLE')
    else :
        for i in range(5) :
               y+=34
        print('Case #'+str(kk+1)+':',*l1)