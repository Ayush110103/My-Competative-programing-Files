s=input()
n=len(s)
x=0
y=0
for i in range(n):
    if(s[i]=="7"):
        y+=1
    elif(s[i]=="4"):
        x+=1
if(x==y==0):
    print(-1)
else:
    if(x>=y):
        print(4)
    else:
        print(7)
