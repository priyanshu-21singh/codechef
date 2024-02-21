# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the rolled number for each test case
    rolled_number = int(input())

    # Check if Chef can enter a new token
    if rolled_number == 6:
        print("YES")
    else:
        print("NO")
