for aa in range(int(input())):
    n=int(input())
    s=(input())
    z=0
    c=0
    x=[]
    for i in s:
        
        if(i=="1"):
            c+=1
        else:
            if(c>0):
             x.append(c)
            c=0
    if(c>0):
             x.append(c)
    # print(x)
    # continue
    
    if(len(x)==1):
        print(x[0])
        continue
    if(x==[]):
        print(0)
        continue
    if(s[0]=="0"):
        print(max(x))
        continue

    if(s[0]=="1"):
        if(x[0]==max(x)):
            x.sort()
            x.reverse()
            print(x[0]+x[1])
        else:
            print(x[0]+max(x))
            
        
        
         
                
            
        

    
        


