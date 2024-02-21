# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input for each test case
    x, y = map(int, input().split())

    # Calculate the minimum amount to invest to avoid taxes
    minimum_investment = max(0, x - y)

    # Print the result for each test case
    print(minimum_investment)
