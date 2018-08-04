'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num_val = int(input())
    if num_val <= 0:
        print()
    for num_vala in range(1, num_val+1):
        if(num_vala%3 == 0 and num_vala%5 == 0):
            print("Fizz")
            print("Buzz")
        elif num_vala%3 == 0:
            print("Fizz")
        elif num_vala%5 == 0:
            print("Buzz")
        else:
            print(num_vala)
if __name__ == "__main__":
    main()
