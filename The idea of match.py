def is_ides_of_march(day):
    return day == 15

# Read input
day = int(input())

# Check if it's the ides of March
if is_ides_of_march(day):
    print("Yes")
else:
    print("No")
