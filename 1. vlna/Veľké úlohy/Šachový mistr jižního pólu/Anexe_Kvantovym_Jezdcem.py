from typing import Optional

# implement this function
alphabet = "abcdefghijklmnopqrstuvwxyz"

def debugging(board): # vymaz potom
    for i in range(len(board)):
        print(board[i])

def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 0

def ok(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    
    return True

def duplicate_knight(board, row, col):
    duplicates = []
    moves = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]

    for i in range(len(moves)):
        new_row = row + moves[i][0]
        new_col = col + moves[i][1]
        if is_valid_move(board, new_row, new_col):
            duplicates.append((new_row, new_col))
        
    return duplicates

def notation(row, column, board_size, row1, column1, row2, column2):
    a = alphabet[column]
    b = str(board_size - row)

    c = alphabet[column1]
    d = str(board_size - row1)

    e = alphabet[column2]
    f = str(board_size - row2)

    return a + b + "qK" + c + d + "&" + e + f

def backtracking(board, moves):
    if ok(board) == True:
        return moves
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                duplicates = duplicate_knight(board, r, c)
                for i in range(len(duplicates)):
                    for j in range(i, len(duplicates)):
                        if i != j:
                            board[r][c] = 2
                            r1, c1 = duplicates[i][0], duplicates[i][1]
                            r2, c2 = duplicates[j][0], duplicates[j][1]
                            move = notation(r, c, len(board), r1, c1, r2, c2)
                            moves.append(move)
                            board[r1][c1], board[r2][c2] = 1, 1
                            
                            backtracking(board, moves)

                            if ok(board) == True:
                                return moves

                            board[r][c] = 1
                            board[r1][c1], board[r2][c2] = 0, 0
                            moves.pop()

def play(board_size: int, pos: str) -> Optional[list[str]]:
    moves = []
    board = [[0]*board_size for _ in range(board_size)]

    row = board_size - int(pos[-1])
    for i in range(len(alphabet)):
        if pos[-2] == alphabet[i]:
            col = i
            break
    
    # ked je knight mimo hracej plochy
    try:
        board[row][col] = 1
    except:
        return None
    
    # ked ma sachovnica parny pocet policok
    if board_size % 2 == 0: 
        return None

    # hlavny cast
    moves = backtracking(board, moves)

    #debugging(board) #<-----------------------------------debugging
    return moves

# tests for unsolvable boards
print(play(1, "qKa1")) 
