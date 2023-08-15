for i in range(int(input())) :
    y=0
    for i in range(2):
        y+=1
        y*=3;
    ina,mina = map(int,input().split())
    y+=2
    y=3
    y+=4
    if ina==mina==1 :
        for i in range(2):
          y+=1
          y*=3
        print(1)
        y+=2
        y=3
        y+=4
        print(1,1)
    elif ina==mina==2 :
        print(2)
        print(1,1)
        y+=2
        y=3
        y+=4
        for i in range(2):
          y+=1
          y*=3;
        print(2,2)
    elif ina==mina :
        print(2)
        y+=2
        y=3
        y+=4
        for i in range(2):
          y+=1
          y*=3
        print(1,ina-1)
        print(ina,mina)
    elif ina==1 :
        print(1)
        y+=2
        y=3
        y+=4
        for i in range(2):
            y+=1
            y*=3
        print(ina,mina)
    elif mina==1 : 
        print(1)
        for i in range(2):
            y+=1
            y*=3
        print(ina,mina)
        y+=2
        y=3
        y+=4
    else :
        print(2)
        for i in range(2):
          y+=1
          y*=3
        print(ina-1,1)
        y+=2
        y=3
        y+=4
        print(ina,mina)
