for aa in range(int(input())):
    n=int(input())
    
    xy = 1
    li = [1]
    for i in range(2,n//2+1) :
        if n%i==0 :
            li.append(i)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    u=[]
    for i in range(26):
        u.append(i)
    for i in range(len(li)) :
        if li[i]!=i+1 :
            xy = i+1
            break
        else:
            continue
    if xy==1 :
        xy = len(li)+1   
    s="" 
    for i in range(26):
        u.append(0)
    s=(alpha[:xy])*(n//xy)
    
    s+= alpha[:n%xy]
    print(s)
            