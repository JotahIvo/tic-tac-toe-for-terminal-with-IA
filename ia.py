def verify_victory(board, player):
        #verificar linhas:
        for i in range(3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                if player == "X":  
                    return 1
                elif player == "O":
                    return -1
                else:
                    return 0 

        #verificar colunas:
        for i in range(3):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                if player == "X":  
                    return 1
                elif player == "O":
                    return -1
                else:
                    return 0

        #verificar diagonais:
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            if player == "X":  
                return 1
            elif player == "O":
                return -1
            else:
                return 0

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            if player == "X":  
                return 1
            elif player == "O":
                return -1
            else:
                return 0    

        return 0  


def ia(board):
    possibilities = all_possibilities(board)
    best_position = None
    max_score = None

    for possibilitie in possibilities:
        board[possibilitie[0]][possibilitie[1]] = "O"
        score = minimax(board)
        board[possibilitie[0]][possibilitie[1]] = " "

        if max_score is None:
            max_score = score
            best_position = possibilitie
        else:
            

    return best_position


def all_possibilities(board):
    positions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                positions.append([i, j])

    return positions


def minimax(board):

