
doors = [0] * 100


for i in range( 101):
    for j in range(i - 1, 100, i):
        
        doors[j] = 1 - doors[j]


for door_number, state in enumerate(doors):
    print(f"Door {door_number + 1} is {'open' if state == 1 else 'closed'}.")