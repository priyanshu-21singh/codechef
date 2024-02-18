def find_max_ones_row(matrix):
    max_ones_count = 0
    max_ones_row = -1

    for i, row in enumerate(matrix):
        ones_count = row.count(1)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_row = i

    return max_ones_row

# Example usage:
matrix = [
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
]

result = find_max_ones_row(matrix)
print(f"The row with the maximum number of 1s is: {result}")

