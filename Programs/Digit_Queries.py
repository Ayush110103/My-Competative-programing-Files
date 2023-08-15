# Consider an infinite string that consists of all positive integers in increasing order:
# 12345678910111213141516171819202122232425...
# Your task is to process q
#  queries of the form: what is the digit at position k
#  in the string
 


for aa in range(int(input())):
    n=int(input())

    if n<=9:
        print(n)
    else:
        i=1
        while n>0:
            n=n-i*9*(10**(i-1))
            i+=1
        i-=1
        n+=i*9*(10**(i-1))
        q,r=divmod(n,i)
        if r==0:
            print(str(10**(i-1)+q-1)[-1])
        else:
            print(str(10**(i-1)+q)[r-1])
            
    
