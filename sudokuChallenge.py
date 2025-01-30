inputOne = """+-------+-------+-------+
| . . 1 | 2 7 5 | . 9 6 |
| 8 5 . | 6 . 3 | 4 . . |
| . . . | . 1 4 | 3 . 2 |
+-------+-------+-------+
| . 3 . | . . . | 7 . . |
| . 2 8 | 3 . . | 9 6 . |
| . 7 . | 9 2 . | 1 . 5 |
+-------+-------+-------+
| . . . | . 4 . | . . 1 |
| 9 . 5 | . . . | 2 4 3 |
| 4 . 7 | . 3 . | . . . |
+-------+-------+-------+"""

# Create a list of digits from the input
returnedNumbers = ''.join(char if char.isdigit() or char == '.' else '' for char in inputOne)

# Convert to 2D list representation of the sudoku puzzle
sudoku = []
for i in range(0, len(returnedNumbers), 9):
    row = [0 if x == '.' else int(x) for x in returnedNumbers[i:i+9]]
    sudoku.append(row)

# Function to check if a number is safe to place
def rowCheck(sudoku, row, col, num):
    # Check if num exists in the row
    if num in sudoku[row]:
        return False
    
    # Check if num exists in the column
    for r in range(9):
        if sudoku[r][col] == num:
            return False
        
    # Check if num exists in the 3x3 subgrid
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
            
    return True

# solve the sudoku
def solve(sudoku, row, col):
    # done if reach end of grid
    if row == 8 and col == 9:
        return True

    # Move to next column, or row if the column is 9
    if col == 9:
        row += 1
        col = 0

    # If the current cell is already filled, skip to next one
    if sudoku[row][col] != 0:
        return solve(sudoku, row, col + 1)

    # Test all possible numbers
    for num in range(1, 10):
        # check if number can be placed
        if rowCheck(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve(sudoku, row, col + 1):
                return True
            sudoku[row][col] = 0  # Recurse of not successful

    return False

# Solving the Sudoku puzzle
def solveSudoku(sudoku):
    solve(sudoku, 0, 0)
    
solveSudoku(sudoku)

# Print the solved sudoku
for row in sudoku:
    print(" ".join(map(str, row)))