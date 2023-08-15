import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    k=[]
    t=li[0]+li[1]
    for i in range(2,n):
        t+=li[i]
        k.append(t)
        t-=li[i-2]
  
    
    f=[]
    for i in range(len(k)):
        if(k[i]%3==0):
            f.append(0)
        else:
            f.append(3-(k[i]%3))
    
    c=0
  
    p=f.copy()
    q=f.copy()
    
    

    for i in range(len(f)):
        if(f[i]==0):
            continue
        else:
            c+=f[i]
            r=f[i]
            for j in range(3):
                if(i+j<len(f)):
                    # print(1)
                    f[i+j]-=r
                    if(f[i+j]<0):
                        f[i+j]=3-abs(f[i+j])
    if(len(f)==1):
        print(c)
        continue
    if(len(f)>1):
        w=[]

        w.append(c)
        c=0
        c+=p[0]
        p[0]=0
        for i in range(len(p)):
            if(p[i]==0):
                continue
            else:
                c+=p[i]
                r=p[i]
                for j in range(3):
                    if(i+j<len(p)):
                        # print(1)
                        p[i+j]-=r
                        if(p[i+j]<0):
                            p[i+j]=3-abs(p[i+j])
        w.append(c)
        c=0
        if(len(q)>1):
            if(q[0]==q[1]):
                c+=q[0]
                q[0],q[1]=0,0
                # print(q)
                for i in range(len(q)):
                  if(q[i]==0):
                      continue
                  else:
                      c+=q[i]
                      r=q[i]
                      for j in range(3):
                          if(i+j<len(q)):
                              # print(1)
                              q[i+j]-=r
                              if(q[i+j]<0):
                                  q[i+j]=3-abs(q[i+j])
                      # print(q)
                w.append(c)
        # print(w)
        print(min(w))


            




        
        
                    
                    
                    
                    
            

                
              
          
            

        
            