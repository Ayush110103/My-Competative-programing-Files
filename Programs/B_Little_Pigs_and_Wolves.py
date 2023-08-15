def gen(a,b,sh):
    li=[[a+1,b],[a-1,b],[a,b+1],[a,b-1]]
    for i in li:
        if(i in sh):
            return True
    
    return False

def pair(a,b,sh):
    li=[[a+1,b],[a-1,b],[a,b+1],[a,b-1]]
    for i in li:
        if(i in sh):
            return i
    
   

n,m=map(int,input().split())
x=[]
y=[]
sheep=[]
wolf=[]
for i in range(n):
    s=input()
    y.append(s)
for i in range(n):
    for j in range(m):
        if(y[i][j]=="W"):
            wolf.append([i,j])
        if(y[i][j]=="P"):
            sheep.append([i,j])
c=0
# print(wolf,sheep)
for i in wolf:
    if(gen(i[0],i[1],sheep)==True):
        c+=1
        sheep.remove(pair(i[0],i[1],sheep))
            
print(c)


        
