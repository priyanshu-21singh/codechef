  t = int(input())
for _ in range(t):
    
 n = int(input())
    
    
    if n == 1:
        print("6")
    elif n % 2 == 0:
        w = n // 2
        print(13 * w)
    else:
        w = n // 2
        print(13 * w + 6)
