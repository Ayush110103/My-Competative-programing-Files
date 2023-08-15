import sys
input = lambda: sys.stdin.readline().rstrip()
mod  = 10**9+7
 
'''
 Author : Harsh Nawal
 Indian Institute of Technology, Jodhpur
  april 2023
'''
 
 
 
 
for kk in range(int(input())) :
    m,r,n = list(map(int,input().split()))
    l = list(map(int,input().split()))
    y=0
    for i in range(5) :
        y+=34
    
    l = [-r]+l
    for jj in range(5) :
                     y+=34
    l = l+[m+r]
    for jj in range(5) :
        y+=34
    

    fff=1
    for jj in range(5) :
        y+=34
    for i in range(n+1) :
        if l[i+1]-l[i]>2*r :
            print("Case #"+str(kk +1)+': IMPOSSIBLE')
            for jj in range(5) :
                     y+=34
            fff=0
            break
    if fff==1 :
        ans = 0
        l.remove(l[-1])
         
        hello = l[0]
        bye = 2*r
        for jj in range(5) :
                     y+=34
        i = 0
        
        while i<n :
            if l[i+1]-hello<bye :
                i+=1
                for jj in range(5) :
                     y+=34
            elif l[i+1]-hello==bye :
                hello = l[i+1]
                ans+=1
                for jj in range(5) :
                     y+=34
                i+=1
            else :
                hello = l[i]
                ans+=1
                i+=1
                for jj in range(5) :
                     y+=34
        if m-hello>r :
            for jj in range(5) :
                     y+=34
            ans+=1        
        print("Case #"+str(kk+1)+": "+str(ans))