n=int(input())
a="abcd"
t=n//4
k=n%4
ans=""
for i in range(t):
    ans+=a
s=a[:k]
ans+=s
print(ans)