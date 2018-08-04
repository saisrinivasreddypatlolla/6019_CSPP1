'''
Given a number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num_val = int(input())
    rem_val = 0
    pro_val = 1
    flag = 0
    if num_val <= 0:
        flag = 1
        num_val = abs(num_val)
    for n_val in str(num_val):
        rem_val = int(n_val)%10
        pro_val *= rem_val
    if flag == 1:
        pro_val = -pro_val
    print(str(pro_val))

if __name__ == "__main__":
    main()
