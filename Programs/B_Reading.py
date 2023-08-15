n,m=map(int,input().split())
li=list(map(int,input().split()))


d={}
for i in range(n):
      if li[i] in d:
            d[li[i]].append(i)
      else:
            d[li[i]]=[i]
         
li.sort()
li.reverse()
print(li[m-1])
t=[]
for i in range(m):
      t.append(d[li[i]][0]+1)
      d[li[i]].pop()
t.sort()

print(*t)




