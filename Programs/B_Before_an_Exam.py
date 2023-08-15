d,s=map(int,input().split())
min=[]
max=[]
for i in range(d):
    a,b=map(int,input().split())
    min.append(a)
    max.append(b)
if(sum(max)<s):
    print("NO")
    quit()
if(sum(min)>s):
    print("NO")
    quit()

print("YES")
k=s-sum(min)
for i in range(d):
    if(k==0):
        break
    if(k>=max[i]-min[i]):
        
        k-=max[i]-min[i]
        min[i]=max[i]
        # print(k)
        continue
    if(k<max[i]-min[i]):
        min[i]=k+min[i]
        break
print(*min)


