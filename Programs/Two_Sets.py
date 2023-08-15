n=int(input())
li=[]
if(n==1 or n==2):
    print("NO")
    quit()
if(n==3):
    print("YES")
    print(1)
    print(3)
    print(2)
    print(1,2)
    quit()
t=int(n*(n+1)/2)
for i in range(n):
    li.append(i+1)

if t%2!=0:
    print("NO")
    quit()
p=[]
j=0
for i in range(n):
    j+=li[n-1-i]
    p.append(j)
# print(p)
k=t//2
o=0
u=-1
for i in range(n):
    if(k<p[i]):
        u=i
        o=p[i-1]
        break
li.reverse()
l=li[:u]+[k-o]
li.remove(k-o)
li.reverse()
li=li[:n-u-1]

print("YES")
print(len(li))
print(*li)
print(len(l))
print(*l)





