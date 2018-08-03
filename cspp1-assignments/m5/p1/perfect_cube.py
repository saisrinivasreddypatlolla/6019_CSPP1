'''# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube'''

def main():
    '''# input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here'''
    num_val = int(input())
    guess = 0
    epsilon = 0.1
    inc = 0.1
    num_a = 0
    while guess < num_val:
        if abs(guess**3-num_val) < epsilon:
            break
        guess = guess+inc
        num_a += 1
    if abs(guess**3-num_val) >= epsilon:
        print(num_val, 'is not a perfect cube')
    else:
        print(num_val, 'is a perfect cube')


if __name__ == "__main__":
    main()
