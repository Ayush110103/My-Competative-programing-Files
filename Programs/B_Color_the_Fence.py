n=int(input())
li=list(map(int,input().split()))
if(n==0):
    print(-1)
    quit()

if(n//min(li)==0):
    print(-1)
    quit()
v=[]
rem=[]

for i in li:
    v.append(n//i)
    rem.append(n%i)

k=max(v)
# print(k)
for i  in range(9):
    if(v[i]==k):
        r=i+1
# print(r)
s=""
for i in range(k):
    s+=str(r)
l=list(map(int,s.strip()))
if(rem[r-1]==0):
    print(s)

    
else:
    t=rem[r-1]
    # print(t)
    c=0
    s=""
    # print(l)
    for i in range(8,r-1,-1):
        print(i)
        while(li[i]-li[r-1]<=t and c<=k-1):
            t-=li[i]-li[r-1]
            # print(li[i]-li[r-1])
            if(i+1>r):
               l[c]=i+1
            # print(l,t)
            c+=1
            
    a=""
    for i in range(k):
        a+=str(l[i])
    print(a)





        

                
        
        


    






    