Function Main
    Declare String Array board[9]
    Declare Integer currentPlayer
    Declare String winner
    Declare Integer move
    Declare Integer userMove
    Declare Integer computerMove

    Assign board[0] = ""
    Assign board[1] = ""
    Assign board[2] = ""
    Assign board[3] = ""
    Assign board[4] = ""
    Assign board[5] = ""
    Assign board[6] = ""
    Assign board[7] = ""
    Assign board[8] = ""
    Assign currentPlayer = Random(2) + 1
    Assign winner = ""
    While winner = ""
        Input move
        If move >= 1 And move <= 9
            Assign board[move - 1] = "O"
            If board[move - 1] = ""
                Assign board[move - 1] = "O"
            End
            If board[0] = "O" And board[1] = "O" And board[2] = "O"
                Assign winner = "User wins"
            End
            Output board[0] & "|" & board[1] & "|" & board[2]
            If board[3] = "O" And board[4] = "O" And board[5] = "O"
                Assign winner = "User wins"
            End
            Output board[3] & "|" & board[4] & "|" & board[5]
            If board[6] = "O" And board[7] = "O" And board[8] = "O"
                Assign winner = "User wins"
            End
            Output board[6] & "|" & board[7] & "|" & board[8]
            If board[0] = "O" And board[3] = "O" And board[6] = "O"
                Assign winner = "User wins"
            End
            If board[1] = "O" And board[4] = "O" And board[7] = "O"
                Assign winner = "User wins"
            End
            If board[2] = "O" And board[5] = "O" And board[8] = "O"
                Assign winner = "User wins"
            End
            If board[0] = "O" And board[4] = "O" And board[8] = "O"
                Assign winner = "User wins"
            End
            If board[2] = "O" And board[4] = "O" And board[6] = "O"
                Assign winner = "User wins"
            End
            Output "Computer's Turn"
            Assign computerMove = Random(9)
            Assign board[computerMove] = "X"
            If board[computerMove] = ""
                Assign board[computerMove] = "X"
            End
            If board[0] = "X" And board[1] = "X" And board[2] = "X"
                Assign winner = "Computer wins"
            End
            Output board[0] & "|" & board[1] & "|" & board[2]
            If board[3] = "X" And board[4] = "X" and board[5] = "X"
                Assign winner = "Computer wins"
            End
            Output board[3] & "|" & board[4] & "|" & board[5]
            If board[6] = "X" And board[7] = "X" And board[8] = "X"
                Assign winner = "Computer wins"
            End
            Output board[6] & "|" & board[7] & "|" & board[8]
            If board[0] = "X" And board[3] = "X" And board[6] = "X"
                Assign winner = "Computer wins"
            End
            If board[1] = "X" And board[4] = "X" And board[7] = "X"
                Assign winner = "Computer wins"
            End
            If board[2] = "X" And board[5] = "X" And board[8] = "X"
                Assign winner = "Computer wins"
            End
            If board[0] = "X" And board[4] = "X" And board[8] = "X"
                Assign winner = "Computer wins"
            End
            If board[2] = "X" And board[4] = "X" And board[6] = "X"
                Assign winner = "Computer wins"
            End
        Else
            Output "Invalid Move"
            Assign board[computerMove] = "O"
        End
    End
    Output Winner
End
