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
    sti_val = ""
    if num_val <= 0:
        print()
    for n in range(1,num_val+1):
        if(n%3 == 0 and n%5 == 0):
            sti_val += "FizzBuzz"
        elif(n%3 == 0):
            sti_val += "Fizz"
        elif(n%5 == 0):
            sti_val += "Buzz"
        else:
            sti_val += str(n)
    print(sti_val)
if __name__ == "__main__":
    main()
