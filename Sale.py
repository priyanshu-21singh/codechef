t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_sales = sum(arr)
    sum_sales += arr[-1]
    max_sales = sum_sales
    
    
    for j in range(n - 2, -1, -1):
        sum_sales = sum_sales + arr[j] - 2 * arr[j + 1]
        if sum_sales >= max_sales:
            max_sales = sum_sales
    
    print(max_sales)
