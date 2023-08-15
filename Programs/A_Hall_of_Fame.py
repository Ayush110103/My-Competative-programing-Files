for aa in range(int(input())):
    n=int(input())
    s=input()
    k=s.count("RL")
    # print(k)
    t=s.count ("LR")
    if(k>0):
        print(0)
        continue
    if(t>0):

        for i in range(n):
            if(s[i]=="L"):
                r=i+1
                continue
        print(r)


      
       
        continue
    if(k==0 and t==0):
        print(-1)
        continue