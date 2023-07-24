def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                # Print the last element of the row without a trailing space
                print("{:d}".format(row[i]))
            else:
                # Print the element followed by a space
                print("{:d}".format(row[i]), end=" ")
