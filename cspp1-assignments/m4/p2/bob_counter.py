'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    ''' this program is used to print the bob count in a given string'''
    STR_A = input()
    COUNT_A = 0
    for CHAR_A in range(len(STR_A) - 2):
        if STR_A[CHAR_A] == 'b' and STR_A[CHAR_A+1] == 'o' and STR_A[CHAR_A+2] == 'b':
            COUNT_A += 1
    print(COUNT_A)
if __name__ == "__main__":
    main()
