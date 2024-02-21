T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    remaining = N - X
    print(remaining)