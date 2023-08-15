import math
n=int(input())
li=list(map(int,input().split()))
k=sum(li)
if(k%3!=0):
    print(0)
    quit()
z=0
for i in li:
    if(i==0):
        continue
    else:
        z=1
        break
if(z==0):
    print(math.comb(n-1,2))
    quit()

        
a=0
d=k/3
c1=0
x=[]
z=0
for i in range(n):
    a+=li[i]
    if(z==1):
        if(a==d):
           c1+=1
        else:
            r=i
            break
    if(z==0):
        
        if(a==d):
            c1+=1
            z=1
    
c2=0
a=0
z=0
for i in range(r,n-1):
    a+=li[i]
    if(z==1):
        if(a==d):
           c2+=1
        else:
            
            break
    if(z==0):
        if(a==d):
            c2+=1
            z=1
# print(c1,c2)
print(c1*c2)  





    


    
