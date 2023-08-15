s=input()
t=input()
if(s.count("tomat")>0):
    print("automaton")
    quit()
d={}
f={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in t:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
z=0
for i in f:
    if i not in d:
        z=1
        break
    
if(z==1):
    print("need tree")
    quit()
if(len(s)==len(t)):
    print("array")
    quit()
if(len(s)!=len(t)):
    print("both")

