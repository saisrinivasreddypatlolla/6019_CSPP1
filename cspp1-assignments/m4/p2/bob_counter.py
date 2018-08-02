'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    ''' this program is used to print the bob count in a given string'''
    str_val = input()
    count_val = 0
    for char_val in range(len(str_val) - 2):
        if str_val[char_val] == 'b' and str_val[char_val+1] == 'o' and str_val[char_val+2] == 'b':
            count_val += 1
    print(count_val)
if __name__ == "__main__":
    main()
