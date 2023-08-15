
s=input()
d={}
for i in range(26):
    d[i]=0
for i in range(len(s)):
    d[ord(s[i])-97]+=1
x=0
for i in d:
    if(d[i]%2!=0):
        x+=1

if(x==0 or x%2!=0):
    print("First")
else:
    print("Second")