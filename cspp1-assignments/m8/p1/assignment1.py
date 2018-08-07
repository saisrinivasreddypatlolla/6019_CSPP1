'''# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and
returns the factorial of given number.

# This function takes in one number and returns one number.
'''
import sys
sys.setrecursionlimit(10000)
def factorial(number):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if number in (1, 0):
        return 1
    return number*factorial(number-1)


def main():
    '''this program is used to print factorial of number using recursion'''
    answer = input()
    print(factorial(int(answer)))

if __name__ == "__main__":
    main()
