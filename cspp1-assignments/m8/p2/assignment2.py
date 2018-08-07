# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(number):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if number <= 0:
        return 0
    return number%10+sumofdigits(number//10)


def main():
    answer = input()
    print(sumofdigits(int(answer)))  

if __name__== "__main__":
    main()

