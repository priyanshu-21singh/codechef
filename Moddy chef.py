def calculate_happiness(N, A, l, r):
    max_happiness = 0
    min_happiness = 0
    count = 0

    for i in range(N):
        if l <= A[i] <= r:
            count += 1
        else:
            count -= 1

        max_happiness = max(max_happiness, count)
        min_happiness = min(min_happiness, count)

    return max_happiness, min_happiness

T = int(input())

for _ in range(T):
    N, l, r = map(int, input().split())
    A = list(map(int, input().split()))
    max_happiness, min_happiness = calculate_happiness(N, A, l, r)
    print(max_happiness, min_happiness)