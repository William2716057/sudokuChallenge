
def replace_dots(input_str):

    return input_str.replace('.', 'X')

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

# Apply the function to replace dots
output_sudoku = replace_dots(input_sudoku)

# Print the modified Sudoku
print(output_sudoku)