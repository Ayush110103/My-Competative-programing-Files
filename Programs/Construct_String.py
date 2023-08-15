for aa in range(int(input())):
    n=int(input())
    s=input()
    k=s[0]
    li=[k]
    e=[]
    c=0
    for i in range(n):
        if(s[i]==k):
            c+=1
        else:
            k=s[i]
            li.append(k)
            
            if(c%2==0 ):
                e.append(2)
            if(c%2!=0):
                e.append(1)
                
            # e.append(int(c/3)+c%3)
            c=1
    if(c%2==0 ):
                e.append(2)
    if(c%2!=0):
                e.append(1)
    t=""
    for i in range(len (li)):
        for j in range(e[i]):
            t+=li[i]
    print(t)
            

