import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

print("TIC-TAC-TOE AI")
print("You are X and Computer is O")
print("AI uses the Minimax algorithm.")
print("Choose positions from 1 to 9.")

while True:
    print_board()

    try:
        player_move = int(input("Enter your move (1-9): ")) - 1

        if player_move < 0 or player_move > 8:
            print("Please enter a number between 1 and 9.")
            continue

        if board[player_move] != " ":
            print("That position is already occupied.")
            continue

        board[player_move] = "X"

        result = check_winner()

        if result:
            print_board()
            print("Result:", result)
            break

        ai_move = computer_move()
        board[ai_move] = "O"

        print("Computer chose position:", ai_move + 1)

        result = check_winner()

        if result:
            print_board()
            print("Result:", result)
            break

    except ValueError:
        print("Please enter a valid number.")
