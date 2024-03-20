def will_switch_ac(temp):
    if temp > 30:
        return "YES"
    else:
        return "NO"

# Taking input
room_temp = int(input().strip())

# Checking if Chef will switch on the AC
result = will_switch_ac(room_temp)

# Printing the result
print(result)
