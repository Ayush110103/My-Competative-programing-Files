n=int(input())
if(n==1):
    print(1)
    quit()
if(n<=3):
    print("NO SOLUTION")
    quit()
li=[]
if(n==4):
    print("3 1 4 2")
    quit()
for i in range(n):
    li.append(i+1)
x=[]
for i in range(n,0,-2):
    x.append(i)
for i in range(n-1,0,-2):
    x.append(i)
    
print(*x)
