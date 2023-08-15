import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200001)
 
c=0
s=""
def is_valid(vis,x,y,n,m):
      if(x<0 or y<0 or x>n or y>m):
                # global c,s
                # c+=1
                return False
  
      if(vis[x][y]==1):
          return False
      
      return True

          
     
def dfs(vis,i,j,n,m):
      if(i==n-1 or i==0 or j==m-1 or j==0):
            # print(i,j)
            return True
      moves=[[-1,0],[1,0],[0,1],[0,-1]]
      vis[i][j]=1
      for k in moves:
            # print(k)
            x=i+k[0]
            y=j+k[1]
            if(is_valid(vis,x,y,n,m)):
                # dfs(vis,x,y,n,m)
              if(dfs(vis,x,y,n,m)):
                  global c,s
                  # print(s)
                  if(k==[-1,0]):
                        s+="U"
                  elif(k==[1,0]):
                        s+="D"
                  elif(k==[0,1]):
                        s+="R"
                  elif(k==[0,-1]):
                        s+="L"
                  # print(s)
                  return True    
      return False
      



    
    
n, m = map(int, input().split()) 
u=[]
for i in range(n):
    o=input()
    u.append(o)

vis=[]
for i in range(n):
    vis.append([])

for i in range(n):
    for j in range(m):
        if(u[i][j]=="M" or u[i][j]=="#"):
            vis[i].append(1)
        elif(u[i][j]=="A"):
            a=i
            b=j
            vis[i].append(0)
        else:
            vis[i].append(0)
u=dfs(vis,a,b,n,m)

# print(s)

if(len(s)>0):
     print("YES")
     print(len(s))
     s=s[::-1]
     print(s)
else:
     print("NO")

     

    






        
 