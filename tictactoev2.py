import random
random.seed()   #Prepare random number generator

board = [""] * (9)

board[0] = " "
board[1] = " "
board[2] = " "
board[3] = " "
board[4] = " "
board[5] = " "
board[6] = " "
board[7] = " "
board[8] = " "
currentPlayer = int(random.random() * 2) + 1
winner = ""
while winner == "":
    move = int(input())
    if move >= 1 and move <= 9:
        board[move - 1] = "O"
        if board[move - 1] == " ":
            board[move - 1] = "O"
        if board[0] == "O" and board[1] == "O" and board[2] == "O":
            winner = "User wins"
        print(board[0] + "|" + board[1] + "|" + board[2])
        if board[3] == "O" and board[4] == "O" and board[5] == "O":
            winner = "User wins"
        print(board[3] + "|" + board[4] + "|" + board[5])
        if board[6] == "O" and board[7] == "O" and board[8] == "O":
            winner = "User wins"
        print(board[6] + "|" + board[7] + "|" + board[8])
        if board[0] == "O" and board[3] == "O" and board[6] == "O":
            winner = "User Wins"
        if board[1] == "O" and board[4] == "O" and board[7] == "O":
            winner = "User wins"
        if board[2] == "O" and board[5] == "O" and board[8] == "O":
            winner = "User wins"
        if board[0] == "O" and board[4] == "O" and board[8] == "O":
            winner = "User wins"
        if board[2] == "O" and board[4] == "O" and board[6] == "O":
            winner = "User wins"
        print("Computer's Turn...")
        computerMove = int(random.random() * 9)
        board[computerMove] = "X"
        if board[computerMove] == " ":
            board[computerMove] = "X"
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            winner = "Computer wins"
        print(board[0] + "|" + board[1] + "|" + board[2])
        if board[3] == "X" and board[4] == "X" and board[5] == "X":
            winner = "Computer wins"
        print(board[3] + "|" + board[4] + "|" + board[5])
        if board[6] == "X" and board[7] == "X" and board[8] == "X":
            winner = "Computer wins"
        print(board[6] + "|" + board[7] + "|" + board[8])
        if board[0] == "X" and board[3] == "X" and board[6] == "X":
            winner = "Computer wins"
        if board[1] == "X" and board[4] == "X" and board[7] == "X":
            winner = "Computer wins"
        if board[2] == "X" and board[5] == "X" and board[8] == "X":
            winner = "Computer wins"
        if board[0] == "X" and board[4] == "X" and board[8] == "X":
            winner = "Computer wins"
        if board[2] == "X" and board[4] == "X" and board[6] == "X":
            winner = "Computer wins"
    else:
        print("Invalid Move")
        board[computerMove] = "O"
print(winner)
