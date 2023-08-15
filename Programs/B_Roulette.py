# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
  # n,m=map(int,input().split())
c=0
x=[]
for i in range(n):
     n=int(input())
     li=list(map(int,input().split()))
     x.append(li)
y=int(input())
min=1000000
k=[]
o=0
for i in  x:
     o+=1
     if(y in i):
          if(min>len(i)):
               c=1
               k=[]
               k.append(o)
               min=len(i)
          elif(min<len(i)):
               continue
          else:
               c+=1
               k.append(o)
          min=len(i)
if(c==0):
     print(0)
else:
     print(c)
     print(*k)




          
          

     
