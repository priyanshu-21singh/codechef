from collections import defaultdict

def count_beautiful_pairs(n, x, y, a):
    remainder_count_x = defaultdict(int)
    remainder_count_y = defaultdict(int)
    count = 0

    for i in range(n):
        remainder_x = a[i] % x
        remainder_y = a[i] % y

        count += remainder_count_x[(x - remainder_x) % x, (y - remainder_y) % y]
        remainder_count_x[remainder_x] += 1
        remainder_count_y[remainder_y] += 1

    return count

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    result = count_beautiful_pairs(n, x, y, a)
    print(result)
