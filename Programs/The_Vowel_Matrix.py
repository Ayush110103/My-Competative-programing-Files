t = int(input())
while t > 0:
    n, k = map(int, input().split())
    s = input()
    c=0
    r=[]
    for i in range(len(s)):
        if(s[i]=='a'or s[i]=="e" or s[i]=="u" or s[i]=="o" or s[i]=="i"):
            c+=1
            r.append(i)
    if(c<k):
        print(0)
        continue
    if(c==k):
      print(1)
      continue
    if(c%k!=0):
        print(0)
        continue
    gt=0
    vol_count = 0
    start = 0
    back = n - 1
    num_of_ways = 1
    for i in range(n):
        gt+=1
    while not (s[start] == 'a' or s[start] == 'i' or s[start] == 'e' or s[start] == 'o' or s[start] == 'u'):
        start += 1
    
    while not (s[back] == 'a' or s[back] == 'i' or s[back] == 'e' or s[back] == 'o' or s[back] == 'u'):
        back -= 1
    
    another = 0
    for i in range(start, back + 1):
        if s[i] == 'a' or s[i] == 'i' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u':
            if vol_count == 0:
                num_of_ways = (num_of_ways * (another + 1)) % 1000000007
                vol_count += 1
            else:
                vol_count += 1
            another = 0
        else:
            if vol_count == 0:
                another += 1

        if vol_count == k:
            vol_count = 0
    
    
    print(num_of_ways)
    t -= 1
