'''This program is to take matrices as input and
    return addition and multiplication of two matrices'''
def mult_matrix(matrix1, matrix2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(matrix1)
    columns = len(matrix2[0])
    values = len(matrix2)
    multiply_matrix = []
    if len(matrix1[0]) == len(matrix2):
        for row in range(rows):
            mult_matrix_row = []
            for column in range(columns):
                mult_matrix_value = 0
                for value in range(values):
                    mult_matrix_value += matrix1[row][value]*matrix2[value][column]
                mult_matrix_row.append(mult_matrix_value)
            multiply_matrix.append(mult_matrix_row)
        return multiply_matrix
    print("Error: Matrix shapes invalid for mult")
    return None

def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    addition_matrix = []
    rows = len(matrix1)
    columns = len(matrix1[0])
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for row in range(rows):
            add_matrix_row = []
            for column in range(columns):
                add_matrix_row.append(matrix1[row][column]+matrix2[row][column])
            addition_matrix.append(list(add_matrix_row))
        return addition_matrix
    print("Error: Matrix shapes invalid for addition")
    return None


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    rows, columns = input().split(',')
    for _ in range(int(rows)):
        row = list(map(int, input().split()))
        assert len(row) == int(columns)
        matrix.append(row)
    # matrix = [list(map(int, input().split())) for row in range(int(rows))]
    return matrix
def main():
    '''
        Initialisation of matrix
        print addition of two matrices
        print multiplication of two matrices
    '''

    # read matrix 1
    try:
        matrix1 = read_matrix()

        # read matrix 2
        matrix2 = read_matrix()
    except AssertionError:
        print("Error: Invalid input for the matrix")

    else:
        # add matrix 1 and matrix 2
        print(add_matrix(matrix1, matrix2))

        # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix1, matrix2))

if __name__ == '__main__':
    main()
