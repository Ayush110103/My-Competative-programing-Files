'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
li=list(map(int,input().split()))
x=[[li[0],1]]
k=[0]

for i in range(1,n):
    while(len(x)>0):
        if(x[len(x)-1][0]<li[i]):
            break
        x.pop()
    if(len(x)>0):
        k.append(x[len(x)-1][1])
    if(len(x)==0):
        k.append(0)
        
    x.append([li[i],i+1])
    
        
print(*k)