'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5'''

def main():
    ''' thisprogram is used to check vowels count in given string'''

STRING_A = input()
COUNT = 0
for char in STRING_A:
    if char in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1
print(COUNT)

    # the input string is in s
    # remove pass and start your code here


if __name__ == "__main__":
    main()
