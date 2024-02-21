# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input for each test case
    x, y = map(int, input().split())

    # Calculate the total amount Chef will have to pay
    total_amount = x * y

    # Print the result for each test case
    print(total_amount)
