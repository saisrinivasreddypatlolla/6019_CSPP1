'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    ''' this function is used to take input as number of lines and sentence in it
        and prints the line'''
    number = int(input())
    for _ in range(number):
        line = input()
        print(line)

if __name__ == '__main__':
    main()
