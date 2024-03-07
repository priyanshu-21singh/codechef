def test_case():
    n = int(input())
    print("ODD" if bin(n).count('1') % 2 else "EVEN")

def main():
    t = int(input())
    for _ in range(t):
        test_case()

if __name__ == "__main__":
    main()
