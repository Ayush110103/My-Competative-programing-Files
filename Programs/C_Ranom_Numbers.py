import sys
input = lambda: sys.stdin.readline().rstrip()
import bisect

def lower_bound(arr, x):
    index = bisect.bisect_left(arr, x)
    return index



for aa in range(int(input())):
    s=input()
    r=-1
    for i in range(len(s)):
        if(s[i]!="E"):
            r=i
            break
    if(r!=-1):
       s=s[:i]+"E"+s[i+1:]
    f={}
    f["A"]=1
    f["B"]=10
    f["C"]=100
    f["D"]=1000
    f["E"]=10000


    # print(s)
    d={}
    x=[]

    for i in range(len(s)):
        if(s[i] in d):
            d[s[i]].append(i)
        else:
            d[s[i]]=[i]
            x.append(s[i])
    x.sort()
    ans=0
    if(len(x)==1):
        
        for i in range(len(s)):
            ans+=f[s[i]]
        print(ans)
        continue
                
    t=x[0]
    for i in range(1,len(x)):
        p=max(d[x[i]])
        y=lower_bound(d[t],p)
        ans+=f[t]*(len(d[t])-y)-f[t]*y
        t=x[i]
    ans+=f[t]*len(d[t])
    print(ans)

        
        
    # print(d)
    
        
