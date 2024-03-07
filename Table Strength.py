def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        legs = list(map(int, input().split()))

        legs.sort()
        maxWeight = 0
        for i in range(N - 1, -1, -1):
            totalWeight = legs[i] * (N - i)
            maxWeight = max(maxWeight, totalWeight)

        print(maxWeight)

if __name__ == "__main__":
    main()
