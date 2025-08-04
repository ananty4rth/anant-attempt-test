# Python script to multiply two 3x3 matrices using while loop

# Define two 3x3 matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Resultant matrix initialized to zero
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Multiplying matrix1 and matrix2
i = 0
while i < 3:
    j = 0
    while j < 3:
        k = 0
        while k < 3:
            result[i][j] += matrix1[i][k] * matrix2[k][j]
            k += 1
        j += 1
    i += 1

# Print the result
print("Resultant Matrix:")
i = 0
while i < 3:
    print(result[i])
    i += 1
