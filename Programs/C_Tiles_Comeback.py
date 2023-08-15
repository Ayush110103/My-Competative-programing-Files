# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    # n=int(input())
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    if(li[0]==li[n-1]):
        o=0
        for i in range(n):
            if(li[i]==li[0]):
                o+=1
        # print(o)
        if(o>=k):
            print("YES")
            continue

    li.reverse()
    
        
    c=0
    for i in range(n):
        if(li[i]==li[0]):
            c+=1
        if(c==k):
            break
    if(i==n-1 and c!=k):
        print("NO")
        continue
    f=li[i+1:]
    t=len(f)
    # print(f)
    c=0
    for i in range(t):
        if(f[i]==f[t-1]):
            c+=1
        if(c==k):
            break
    if(c==k):
        print("YES")
    else:
        print("NO")
        
            