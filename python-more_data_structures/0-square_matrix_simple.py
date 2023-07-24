def square_matrix_simple(matrix=[]):
    # Create an empty new_matrix with the same size as the input matrix
    new_matrix = [[0 for _ in row] for row in matrix]

    # Iterate through each element of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Calculate the square value of the current integer and store it in the new matrix
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
