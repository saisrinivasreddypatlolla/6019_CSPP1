'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''print the given number is perfect squre or not using newtons rapson method'''
    num_val = int(input())
    guess = num_val/2.0
    epsilon = 0.01
    while (guess*guess-num_val) >= epsilon and guess <= num_val:
        guess = guess-(((guess**2)-num_val)/(2*guess))
    print(guess)

if __name__ == "__main__":
    main()
