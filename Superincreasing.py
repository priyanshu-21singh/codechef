def main():
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        if k > 2:
            if 2 ** (k - 1) <= x:
                print("Yes")
            else:
                print("No")
        elif k == 2:
            if x > 1:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    main()
