def can_complete_assignments(T, test_cases):
    for i in range(T):
        X = test_cases[i]
        total_time_needed = 3  # 3 assignments
        start_time = X
        completion_time = start_time + total_time_needed
        if completion_time <= 10:
            print("Yes")
        else:
            print("No")

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    X = int(input())
    test_cases.append(X)

# Check if Janmansh can complete assignments on time
can_complete_assignments(T, test_cases)
