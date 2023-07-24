def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        # Check if the matrix is empty or contains an empty row
        print()
        return

    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]))
            else:
                print("{:d}".format(row[i]), end=" ")
