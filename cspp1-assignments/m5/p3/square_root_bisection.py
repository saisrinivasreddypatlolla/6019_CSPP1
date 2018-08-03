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
    ''' this program is used to print the squareroot value of
    the given number using bi-section method'''
    num_val = int(input())
    epsilon = 0.01
    low = 0
    high = num_val
    avg = (low+high)/2
    while abs(avg**2-num_val) >= epsilon:
        if avg**2 < num_val:
            low = avg
        else:
            high = avg
        avg = (low+high)/2
    print(avg)
if __name__ == "__main__":
    main()
