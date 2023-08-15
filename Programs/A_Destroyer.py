import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    k=li[n-1]
    d={}
    for i in li:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    z=0
    
    x=[]
    for i in d:
        x.append(i)
    x.sort()
    t=x[0]
    if(x[0]!=0):
        print("NO")
        continue
    if(len(d)==1):
        print("YES")
        continue
    for i in range(1,len(x)):
        if i not in d:
            z=1
            break
        
        if((d[x[i]]>d[t]) or x[i]-t!=1 ):
            z=1
            break
        t=x[i]
    if(z==1):
        print("NO")
        continue
    print("YES")

            


        