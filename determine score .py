
def calculate_score(T, test_cases):
    scores = []
    for X, N in test_cases:
        if N == 10:
            score = X
        else:
            score = X * N // 10
        scores.append(score)
    return scores

T = int(input())
test_cases = []
for _ in range(T):
    X, N = map(int, input().split())
    test_cases.append((X, N))

scores = calculate_score(T, test_cases)
for score in scores:
    print(score)