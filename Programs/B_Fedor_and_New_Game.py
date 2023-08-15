n,m,k=map(int,input().split())
# if(n==k):
#     print(n)
#     quit()
li=[]
for i in range(m+1):
    li.append(int(input()))

x=[]
for i in li:
    x.append(bin(i)[2:][::-1])
y=[]
for i in x:
    if(len(i)<n):
        for j in range(n-len(i)):
            # print(i)
            i+="0"
    y.append(i)
# print(y)
r=y[m]
z=r.count("1")
e=0
y.pop(m)
# print(y,r)
for i in y:
    c=0
    for j in range(n):
        if(int(i[j])^int(r[j])==1):
            
                c+=1
    # print(c)
    if(c<=k):
        e+=1
print(e)

        




