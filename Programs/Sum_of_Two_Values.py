import sys
input = lambda: sys.stdin.readline().rstrip()


n,s=map(int,input().split())

li=list(map(int,input().split()))
k=li.copy()




li.sort()
# print(li)

i=0
j=n-1
x,y=0,0
while(i<j):
    if(li[i]+li[j]!=s):
        if(li[i]+li[j]>s):
            j-=1
        else:
            i+=1
    else:
        x,y=li[i],li[j]
        # print(x,y)
        break
if(x==0 and y==0):
    print("IMPOSSIBLE")
else:
    o=[]
    for i in range(n):
        if(k[i]==x):
            o.append(i+1)
            break
    for i in range(n):
        if(k[i]==y and i!=o[0]-1):
            o.append(i+1)
            break
    o.sort()
    print(*o)
    
        

       
    
    
    