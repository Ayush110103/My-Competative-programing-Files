for aa in range(int(input())):
    n=(input())
    x="314159265358979323846264338327"
    c=0
    for i in range(len(n)):
        if(n[i]==x[i]):
            c+=1
        else:
            break
    print(c)