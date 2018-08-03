'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
	    '''this program is used to check given number is perfect square or not'''
    num_val = int(input())
    guess = 0
    epsilon = 0.1
    inc = 0.1
    num_a = 0
    while guess < num_val:
        if abs(guess**2-num_val) < epsilon:
            break
        guess = guess+inc
        num_a += 1
    if abs(guess**2-num_val) >= epsilon:
        print(num_val, 'is not a perfect square')
    else:
        print(num_val, 'is a perfect square')

if __name__ == "__main__":
    main()


if __name__== "__main__":
	main()
