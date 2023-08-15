n,m=map(int,input().split())
li=list(map(int,input().split()))
x=[]
for i in li:
    
    if(i<0):
        x.append(abs(i))
# print(x)
if(li==[]):
    print(0)
    quit()
x.sort()
x.reverse()

if(len(x)<=m):
    print(sum(x))
else:
    print(sum(x[:m]))
    
