import random

def print_sudoku_with_lines(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Horizontal Lines

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  # Vertical Pipes

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


# Validation Control
def is_valid(grid, row, col, num):
    # Row Control
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Column Control
    for i in range(9):
        if grid[i][col] == num:
            return False

    # 3x3 Grid Control
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Empty (9x9) Grid Slots
sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

# Sudoku Filler
def fill_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                num_list = list(range(1, 10))
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if fill_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True


fill_sudoku(sudoku_grid)

print_sudoku_with_lines(sudoku_grid)