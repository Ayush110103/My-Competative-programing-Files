def can_place(x, y, board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'Q' and (x == i or y == j or x+y==i+j or x-y == i-j):
                return False
    return True

def count_placements(board, queens, row):
    if queens == 8:
        return 1
    count = 0
    for col in range(8):
        if board[row][col] == '.' and can_place(row, col, board):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            count += count_placements(board, queens+1, row+1)
            board[row] = board[row][:col] + '.' + board[row][col+1:]
    return count

board = [input() for _ in range(8)]
print(count_placements(board, 0, 0))


        