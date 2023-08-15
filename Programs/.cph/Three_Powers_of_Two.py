for aa in range(int(input())):
    n=int(input())
    s=(input())
    a=s.count("1")
    if(a>3):
        print("NO")
        continue
    if(a==3):
        print("YES")
        continue
    if(a==2):
        if(s.count("10")>0):
            print("YES")
            continue
        else:
            print("NO")
            continue
    if(a<2):
        print("NO")
        continue

  
