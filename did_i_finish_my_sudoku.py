def done_or_not(board):
#checks rows for uniqueness
    for row in board:
        if len(row) > len(set(row)) :
            return 'Try again!'
#checks columns for uniqueness
    for i in range(9):
        collist=[]
        for column in board:
            collist.append(column[i])
        if len(collist) > len(set(collist)) :
            return 'Try again!'
#checks squares for uniqueness
    squares=[board[n][m:m+3] + board[n+1][m:m+3] +  board[n+2][m:m+3] 
                for n in range(0,9,3) for m in range(0,9,3)] 
    for square in squares:
        if len(square) > len(set(square)) :
            return 'Try again!'
    return 'Finished!'