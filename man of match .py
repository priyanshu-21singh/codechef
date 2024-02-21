# Number of test cases
T = int(input())

for _ in range(T):
    # Initialize variables to store the maximum score and the corresponding player index
    max_score = -1
    man_of_the_match = -1

    # Process each player's data
    for i in range(1, 23):
        runs, wickets = map(int, input().split())

        # Calculate the score for each player
        score = runs + (wickets * 20)

        # Update the "Man of the Match" if the current player has a higher score
        if score > max_score:
            max_score = score
            man_of_the_match = i

    # Output the index of the "Man of the Match" for the current test case
    print(man_of_the_match)
