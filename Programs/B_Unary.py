s=input()
d={}
d[">"]=1000
d["<"]=1001
d[","]=1101
d["."]=1100
d["+"]=1010
d["-"]=1011
d["["]=1110
d["]"]=1111
k=""
for i in s:
    k+=str(d[i])
# print(k)
g=k[::-1]
# print(g)
a=0
for i in range(len(g)):
    # print(a)
    if(g[i]=="1"):
       a=a+2**(i)
       a=a%1000003
print(a)

