n=int(input())
if(n<5):
    print(0)
    quit()
l=[5]
for i in range(1000):
    l.append(l[i]*5)
r=i
# print(l[:10])
for i in range(100000):
    if(n<l[i]):
        r=i
        break
c=0
for i in range(i):
    c+=n//l[i]
print(c)

        
