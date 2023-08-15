
for kk in range(int(input())):
  x,y=map(int,input().split())
  p=max(x,y)
  q=min(x,y)

  t=p**2-p+1
  ans=0

  if(p==q):
      print(t)
      continue

  if(x==p):
      if(p%2==0):
          ans=t+p-q
      else:
          ans=t-(p-q)
  if(y==p):
      if(p%2==0):
          ans=t-(p-q)
         
      else:
          ans=t+p-q
  print(ans)