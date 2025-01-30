def find_and_replace_neighbors(input_str):
    # Convert the string into a 2D list (grid)
    grid = [list(line.strip()) for line in input_str.splitlines() if line.strip()]
    
    # Function to check and replace neighbors of 8
    def replace_neighbors():
        # Define the relative positions for neighbors (vertical, horizontal, and diagonal)
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '8':  # If current cell is '8'
                    for dr, dc in neighbors:  # Check all neighbors
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc].isdigit():
                            # Replace the neighbor with '7' if it's a number
                            grid[nr][nc] = '7'

    # Call the function to replace neighbors of '8'
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

# Apply the function to replace neighbors of 8 with 7
output_sudoku = find_and_replace_neighbors(input_sudoku)

# Print the modified Sudoku
print(output_sudoku)
