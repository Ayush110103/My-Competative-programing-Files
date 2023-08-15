n=int(input())
d={}
if n==1:
    print(1)
    quit()
while(True):
    if(n%2==0):
        
        if(n in d):
            d[n]+=1
        else:
            d[n]=1
        n=n//2
    else: 
        if(n in d):
            d[n]+=1
        else:
            d[n]=1
        n=3*n+1
    if(n==1):
        d[1]=1
        break
x=[]
for i in d:
    x.append(i)
print(*x)
    
