def find_number_of_notes(n):
    # Calculate the total amount using Rs. 2000 notes
    total_amount = n * 2000
    
    # Calculate the number of Rs. 500 notes needed
    number_of_500_notes = total_amount // 500
    
    return number_of_500_notes

# Input the number of Rs. 2000 notes Chef has collected
n = int(input())

# Output the number of Rs. 500 notes needed
result = find_number_of_notes(n)
print(result)
