
# guessed the algorith to be used
# In this case it was longest palindromic subsequnence
for aa in range(int(input())):
    n,kl=map(int,input().split())
    s=input()
    # if(s.count("0")==0):
    #     print(0)
    #     continue
    
    c=0
    x=[]
    st=[]
    en=[]
    for i in range(n):
        if(s[i]=="1"):
            if(c==0):
                st.append(i)

            c+=1
        else:
            if(c>0):
                en.append(i)
                x.append(c)
            c=0
    if(c>0):
        x.append(c)
    c=0
    if(x==[] ):
        print(1)
        continue
    z=0
    for i in range(len(x)):
        if(x[i]>=kl):
            z=1
            break
    if(z==1):
        print(0)
        continue
    #start
    # print(x)
    k=x.index(max(x))  
    if(max(x)==1):
        k=len(st)-1
    d=max(x)
    y=[]
    r=st[:k+1]
    t=x[:k+1]
    r.reverse()
    t.reverse()
    # print(r,t)
    # print(k)
    if(len(x)==1):
        y.append(r[0])
       
    else:
        for i in range(0,k):

            y.append(r[i]-r[i+1]-1)
            y.append(t[i+1])
    # print(y)
    c=0
    
    # print(y)
    for i in range(len(y)):
        c+=1
        
        d+=y[i]
        # print(c,d,kl)
        if(d>=kl):
            break
       

    print(c)




            
    
