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

print(returnedNumbers)

separated = "" 
for i in range(0, len(returnedNumbers), 9):
    separated += returnedNumbers[i:i+9] + '\n'
print(separated)

