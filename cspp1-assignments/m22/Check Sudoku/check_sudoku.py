'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''


def column_check(sudoku, list1):
    '''This fuction is used to check the columns and return boolean values'''
    count = 0
    length = len(sudoku)
    temporary_list = []
    for column in range(length):
        list_for_row = []
        for value in range(length):
            list_for_row.append(sudoku[value][column])
        temporary_list.append(list_for_row)
    for column in temporary_list:
        sorted_list = sorted(column)
        if list1 == sorted_list:
            count += 1
        else:
            return False
    return count == len(sudoku)

def row_check(sudoku, list1):
    '''This function is used to check the rows and return bool value'''
    count = 0
    for row in sudoku:
        sorted_list = sorted(row)
        if list1 == sorted_list:
            count += 1
        else:
            return False
    return count == len(sudoku)

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if row_check(sudoku, list1) and column_check(sudoku, list1):
        return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = list(map(int, input().split(' ')))
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
