def max_beauty(n, arr):
    arr.sort(reverse=True)
    beauty = 0
    for i in range(1, n):
        beauty += arr[i-1] - arr[i]
    return beauty

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = max_beauty(n, arr)
        print(result)

if __name__ == "__main__":
    main()