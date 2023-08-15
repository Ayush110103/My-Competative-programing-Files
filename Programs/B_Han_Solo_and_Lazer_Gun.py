def slope(a,b,c,d):
    if(c-a)==0:
        return 'a'
    x=(d-b)/(c-a)
    return x
n,x,y=map(int,input().split())
li=[]

for i in range(n):
    sub=list(map(int,input().split()))
    li.append(slope(x,y,sub[0],sub[1]))
d={}
for i in li:
    if(i in d):
        continue
    else:
        d[i]=1
print(len(d))



