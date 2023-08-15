
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
C=0
i=0
j=n-1
while(i<=j):
    if(i==j):
        C+=1
        break
    if(l[i]+l[j]<=m):
        C+=1
        i+=1
        j-=1
    elif(l[i]+l[j]>m):
        j-=1
        C+=1
print(C)
        
    
  


    

    
        
        
    

    