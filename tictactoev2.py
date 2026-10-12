import random

random.seed()

board = [" "] * 9
currentPlayer = random.randint(1, 2)
winner = ""

def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def check_winner(symbol):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == symbol:
            return True

    return False

print("Tic-Tac-Toe!")
print("Choose a position from 1 to 9.")
print("Positions:")
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")

while winner == "":
    # User's turn
    try:
        move = int(input("Your move (1-9): "))
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if move < 1 or move > 9:
        print("Invalid move! Choose a number from 1 to 9.")
        continue

    if board[move - 1] != " ":
        print("That position is already occupied!")
        continue

    board[move - 1] = "O"
    print_board()

    if check_winner("O"):
        winner = "User wins"
        break

    if " " not in board:
        winner = "It's a draw!"
        break

    # Computer's turn
    print("Computer's turn...")

    empty_positions = [
        i for i in range(9) if board[i] == " "
    ]
    computerMove = random.choice(empty_positions)
    board[computerMove] = "X"

    print_board()

    if check_winner("X"):
        winner = "Computer wins"
        break

    if " " not in board:
        winner = "It's a draw!"
        break

print(winner)
