def sum_digit(n):
     k=0
     for  i in n:
        k+=int(i)
     return k

for aa in range(int(input())):

    n=(input())
   
    for i in range(1,100):
        if(0<=sum_digit(str(i))-sum_digit(str(int(n)-i))<=1):
            print(int(n)-i,i)
            break
    
            
               
    


