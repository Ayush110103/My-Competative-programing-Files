n,k=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in a:
    if(i in d):
      d[i]+=1
    else:
        d[i]=1
m=min(a)
if(m<=k):
    t=2*m +(k-m)

    if(max(a)>t):
        print("NO")
        quit()
    else:
        print("YES")
        for i in range(n):
            b=[]
            if(a[i]>k):
                y=a[i]-k
                for j in range(k):
            
                    b.append(j+1)
                for j in range(y):
                    b.append(j+1)


                




            if(a[i]<=k):
                for i in range(a[i]):
                    b.append(i+1)
                
            print(*b)


if(m>k):
    r=m//k
    e=m%k
  
    if(max(a)>(r+1)*k+e):
        print("NO")
        quit()
    else:
        print("YES")
        w=[]
        for i in range(r):
            for j in range(k):
                w.append(j+1)
        for i in range(e):
            w.append(i+1)
        # w.sort()
        
        for i in range(n):
            
            if(a[i]==m):
                b=[]
            
            if(a[i]>m):
                b=[]
                h=a[i]-m
                if(h<=n):
                   for j in range(h):
                     b.append(j+1)
                if(h>n):
                   for j in range(h):
                     b.append(j+1)
                   for j in  range(h-n):
                      b.append(j+1)
            
            x=w+b 

            print(*x)  
        
                       




            




      