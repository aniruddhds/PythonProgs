import time

def create_board(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for i in range(cols):
            row.append(0)
        board.append(row)
    return board
    
def print_board(board):
    for row in board:
        line = '--'
        for cell in row:
            line += 'x' if cell else '--'  # Print block for alive, space for dead
        print(line)

def count_alive_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r == row and c == col) or r < 0 or c < 0 or r >= rows or c >= cols:
                continue
            if board[r][c] == 1:
                count += 1
    return count

def next_generation(board):
    rows = len(board)
    cols = len(board[0])
    new_board = create_board(rows, cols)
    for r in range(rows):
        for c in range(cols):
            alive_neighbors = count_alive_neighbors(board, r, c)
            if board[r][c] == 1:
                # Rule 1 & 3: Any live cell with fewer than 2 or more than 3 live neighbors dies
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_board[r][c] = 0
                else:
                    # Rule 2: Any live cell with 2 or 3 live neighbors lives on
                    new_board[r][c] = 1
            else:
                # Rule 4: Any dead cell with exactly 3 live neighbors becomes alive
                if alive_neighbors == 3:
                    new_board[r][c] = 1
    return new_board

rows, cols = 20, 40  # Board size
board = create_board(rows, cols)
# Initial pattern (Glider)
glider = [(1,2), (2,3), (3,1), (3,2), (3,3)]
for r, c in glider:
    board[r][c] = 1
try:
    while True:
        print_board(board)
        board = next_generation(board)
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\nGame stopped.")
