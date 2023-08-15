def main():
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        arr3 = list(map(int, input().split()))
        
        initial = 0
        for i in range(n):
            if ((initial | arr1[i]) | m) == m:
                initial = initial | arr1[i]
            else:
                break
        
        for i in range(n):
            if ((initial | arr2[i]) | m) == m:
                initial = initial | arr2[i]
            else:
                break
        
        for i in range(n):
            if ((initial | arr3[i]) | m) == m:
                initial = initial | arr3[i]
            else:
                break
        
        if initial == m:
            print("Yes")
        else:
            print("No")
        
        t -= 1

if __name__ == "__main__":
    main()
