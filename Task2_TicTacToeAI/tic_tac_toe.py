def display(board_state):
    for row in board_state:
        print(" | ".join(row))
    print()

def check_win(board_state):
    win_conditions = board_state + [[board_state[r][c] for r in range(3)] for c in range(3)]

    win_conditions += [
        [board_state[i][i] for i in range(3)],
        [board_state[i][2 - i] for i in range(3)]
    ]

    for item in win_conditions:
        if item == ["X", "X", "X"]:
            return "X"
        if item == ["O", "O", "O"]:
            return "O"

    return None

def is_full(board_state):
    return all(cell != " " for row in board_state for cell in row)

def find_best(board_state, ai_turn):
    winner_status = check_win(board_state)

    if winner_status == "O":
        return 1
    if winner_status == "X":
        return -1
    if is_full(board_state):
        return 0

    scores = []

    for i in range(3):
        for j in range(3):
            if board_state[i][j] == " ":
                board_state[i][j] = "O" if ai_turn else "X"
                scores.append(find_best(board_state, not ai_turn))
                board_state[i][j] = " "

    return max(scores) if ai_turn else min(scores)

def bot_move(board_state):
    best_score = -2
    best_move = None

    for i in range(3):
        for j in range(3):
            if board_state[i][j] == " ":
                board_state[i][j] = "O"
                score = find_best(board_state, False)
                board_state[i][j] = " "

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board_state[best_move[0]][best_move[1]] = "O"

grid = [[" "] * 3 for _ in range(3)]

print("Tic-Tac-Toe AI")
print("Human = X")
print("AI = O")

print("\nPositions:")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")

while True:
    display(grid)

    try:
        choice = int(input("Choose position (1-9): ")) - 1

        if choice < 0 or choice > 8:
            print("Enter a valid number between 1 and 9.")
            continue

        row = choice // 3
        col = choice % 3

        if grid[row][col] != " ":
            print("Position already occupied.")
            continue

        grid[row][col] = "X"

        if check_win(grid) or is_full(grid):
            break

        bot_move(grid)

        if check_win(grid) or is_full(grid):
            break

    except ValueError:
        print("Please enter a valid number.")

display(grid)

winner_status = check_win(grid)

if winner_status == "O":
    print("Winner: AI Unbeatable")
elif winner_status == "X":
    print("Winner: Human Unbeatable")
else:
    print("Match Draw")
