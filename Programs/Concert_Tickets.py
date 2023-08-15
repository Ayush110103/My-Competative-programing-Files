def Bs(arr, a, ss, ee):
         if(ss<ee):
               if(arr[(ss+ee)//2]<a):
        
                         return Bs(arr, a, (ss + ee) // 2 + 1, ee);
               
               if(arr[(ss+ee)//2]>a):
        
                          return Bs(arr, a, ss, (ss + ee) // 2 - 1);
               

               
               return (ss + ee) // 2
            
         
         else:
             
               return ss
         


n,m=map(int,input().split())
t=list(map(int,input().split()))
l=list(map(int,input().split()))
t.sort()

print(t)

# l.sort() 
k=[]
for i in range(n):
    k.append(-1)
i=0
j=0
r=-1
f=l[1]+1
print(Bs(t,f,0,n-1))
# for i in range(m):
    
    


    
        