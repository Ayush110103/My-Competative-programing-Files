s=input()
c=1
t=s[0]
m=-1
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        c+=1
    else:
        if(m<c):
            m=c
        c=1
if(m<c):
    m=c
print(m)
    