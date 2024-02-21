# Input
A, B = map(int, input().split())

# Calculate the sum and append an extra 1
result = A + B

# Append an extra 1 to the result
result_with_extra_1 = result * 10 + 1

# Output the result
print(result_with_extra_1)
