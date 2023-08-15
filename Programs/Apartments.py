n,m,k=map(int,input().split())
l=list(map(int,input().split()))
size=list(map(int,input().split()))
l.sort()
size.sort()
c=0
i=0
j=0
while(i<n):
    if(j<m and abs(size[j]-l[i])<=k):
        c+=1
        i+=1
        j+=1
    elif(j<m and l[i]+k>size[j]):
        j+=1
    elif(j<m and l[i]-k<size[j]):
        i+=1
    elif(j==m):
        break
print(c)
