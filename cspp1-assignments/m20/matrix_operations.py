def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mult_matrix = []
    if len(m1[0]) == len(m2):
        for row in range(len(m1)):
            mult_matrix_row = []
            for column in range(len(m2[0])):
                mult_matrix_value = 0
                for value in range(3):
                    mult_matrix_value += m1[row][value]*m2[value][column]
                mult_matrix_row.append(mult_matrix_value)
            mult_matrix.append(mult_matrix_row)
        return mult_matrix
    else:
        print("Error: Matrix shapes invalid for mult")

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_matrix = []
    rows = len(m1)
    columns = len(m1[0])
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for row in range(rows):
            add_matrix_row = []
            for column in range(columns):
                add_matrix_row.append(m1[row][column]+m2[row][column])
            add_matrix.append(list(add_matrix_row))
        return add_matrix
    print("Error: Matrix shapes invalid for addition")


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    # matrix = []
    rows,columns = input().split(',')
    matrix = [list(map(int, input().split())) for row in range(int(rows))]
    return matrix
def main():
    # read matrix 1
    matrix1 = read_matrix()

    # read matrix 2
    matrix2 = read_matrix()

    # add matrix 1 and matrix 2
    print(add_matrix(matrix1, matrix2))

    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix1, matrix2))

if __name__ == '__main__':
    main()
