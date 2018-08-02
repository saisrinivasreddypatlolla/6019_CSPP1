'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    ''' this program is used to print the bob count in a given string'''
    STR_VAL = input()
    COUNT_VAL = 0
    for CHAR_VAL in range(len(STR_VAL) - 2):
        if STR_VAL[CHAR_VAL] == 'b' and STR_VAL[CHAR_VAL+1] == 'o' and STR_VAL[CHAR_VAL+2] == 'b':
            COUNT_VAL += 1
    print(COUNT_VAL)
if __name__ == "__main__":
    main()
