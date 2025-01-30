import sys
import re

def parse_input():
    grid = []
    for line in sys.stdin:
        if '|' in line:  # Extract only numbers and '.' from the input
            numbers = re.findall(r'[0-9.]', line)
            if numbers:
                grid.append([int(n) if n != '.' else 0 for n in numbers])
    return grid

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def print_grid(grid):
    print("+-------+-------+-------+")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            print(grid[i][j], end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")

grid = parse_input()
solve_sudoku(grid)
print_grid(grid)