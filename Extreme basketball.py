# Function to calculate the number of steps required
def calculate_steps(a, b):
    if a - b > 10:
        return 0
    else:
        b += 10
        temp = b - a
        if temp % 3 != 0:
            return temp // 3 + 1
        else:
            return temp // 3

# Main function
def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        steps = calculate_steps(a, b)
        print(steps)

# Execute main function
if __name__ == "__main__":
    main()
