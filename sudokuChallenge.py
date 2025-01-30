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

returnedNumbers = ''.join(char if char.isdigit() or char == '.' else '' for char in inputOne)

#print(returnedNumbers)

sudoku = "" 
for i in range(0, len(returnedNumbers), 9):
    sudoku += returnedNumbers[i:i+9] + '\n'
print(sudoku)

#check if number exists 
def rowCheck(sudoku, row, col, num):
#check if exists in row    
    for x in range(9):
        if sudoku[row][x] == num:
            return False
 #check if exists in column
    for x in range(9):
        if sudoku[x][col] == num:
            return False
        
    #check if number exists in each square
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    
    for i in range(3):
        for j in range(3):
            if sudoku[i + startRow][j + startCol] == num:
                return False
            
    return True

#solving function
def solve(sudoku, row, col):
    #final position 
    if row == 8 and col == 9:
        return True
    
