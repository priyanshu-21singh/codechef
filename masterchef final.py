# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the current rank of Chef for each test case
    chef_rank = int(input())

    # Check if Chef made it to the top 10
    if chef_rank <= 10:
        print("YES")
    else:
        print("NO")
