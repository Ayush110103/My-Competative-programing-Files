s=input()
d={}
for i in s:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
# print(d)
c=0
for i in d:
    if(d[i]%2!=0):
        c+=1 
if(len(s)%2==0):
    if(c>0):
        print("NO SOLUTION")
        quit()
if(len(s)%2!=0):
    if(c!=1):
        print("NO SOLUTION")
        quit()
l=[]
y=""
d[y]=0
for i in d:
    if(d[i]%2==0):
        l.append(i*(d[i]//2))
    if(d[i]%2!=0):
        y=i

l.sort()
# print(l)
l=l+[y*(d[y])]+l[::-1]
# print(l)
print("".join(l))
