def find_and_replace_neighbors(input_str):
    # Convert the string into a 2D list (grid)
    grid = [list(line.strip()) for line in input_str.splitlines() if line.strip()]

    # Function to check and replace entire row/column of neighbors of '8'
    def replace_neighbors():
        # List to store rows and columns that should be modified
        rows_to_modify = set()
        cols_to_modify = set()

        # Traverse the grid and find every 8
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '.':  # If we find an '.'
                    rows_to_modify.add(r)  # Mark the row to be modified
                    cols_to_modify.add(c)  # Mark the column to be modified

        # Replace the entire rows and columns with '7'
        for r in rows_to_modify:
            for c in range(len(grid[r])):
                if grid[r][c].isdigit():  # Only replace digits
                    grid[r][c] = '7'

        for c in cols_to_modify:
            for r in range(len(grid)):
                if grid[r][c].isdigit():  # Only replace digits
                    grid[r][c] = '7'

    # Call the function to replace neighbors of '8' with '7'
    replace_neighbors()

    # Convert the grid back to a string
    return "\n".join("".join(row) for row in grid)

# Input string
input_sudoku = """
+-------+-------+-------+
| 2 4 . | 8 . 9 | 1 . . |
| . . 8 | 7 6 . | . . . |
| 5 3 . | 2 1 4 | . . . |
+-------+-------+-------+
| . . 2 | 4 9 6 | . . . |
| 9 . 4 | . 3 8 | . . . |
| . 8 5 | 1 . 7 | . . 9 |
+-------+-------+-------+
| . 5 . | . . . | . 8 . |
| . . . | 3 . . | . . 6 |
| 8 . 1 | 6 . 5 | 9 3 4 |
+-------+-------+-------+
"""

# Apply the function to replace rows/columns of 8 with 7
output_sudoku = find_and_replace_neighbors(input_sudoku)

# Print the modified Sudoku
print(output_sudoku)

#matrix1 = []
#matrix2 = []
#matrix3 = []

#matrix4 = []
#matrix5 = []
#matrix6 = []

#matrix7= []
#matrix8 = []
#matrix9 = []

"""
+-------+-------+-------+
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
+-------+-------+-------+
"""

matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
string = "| . . 1 | 2 7 5 | . 9 6 |"

# Initialize variables to track which matrix to add to
current_matrix = 1

for i, char in enumerate(string):
    if char == '|':
        if current_matrix == 1:
            current_matrix = 2
        elif current_matrix == 2:
            current_matrix = 3
        elif current_matrix == 3:
            current_matrix = 4
        elif current_matrix == 4:
            current_matrix = 1
    else:
        if current_matrix == 1:
            matrix1.append((i, char))
        elif current_matrix == 2:
            matrix2.append((i, char))
        elif current_matrix == 3:
            matrix3.append((i, char))
        elif current_matrix == 4:
            matrix4.append((i, char))

# Print the matrices
print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Matrix 3:", matrix3)
print("Matrix 4:", matrix4)