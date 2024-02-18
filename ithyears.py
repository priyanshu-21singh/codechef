t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    answer = v[0]
    for i in range(1, n):
        if v[i] > answer:
            answer = v[i]
        else:
            xx = answer // v[i]
            if xx * v[i] > answer:
                answer = xx * v[i]
            else:
                answer = (xx + 1) * v[i]

    print(answer)