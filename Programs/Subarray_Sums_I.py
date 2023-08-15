'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''



n,s=map(int,input().split())
li=list(map(int,input().split()))
p=[]
d={}
d[0]=1
c=0
r=0
for  i in range(n):
    r+=li[i]
    if(r-s not in d):
        d[r-s]=0
        
    c+=d[r-s]
    if(r not in d):
        d[r]=1
    else:
       d[r]+=1
print(c)
    