'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5'''

def main():
    ''' thisprogram is used to check vowels count in given string'''

    str_value = input()
count_c = 0
for char in str_value:
    if char in ('a', 'e', 'i', 'o', 'u'):
        count_c += 1
print(count_c)

    # the input string is in s
    # remove pass and start your code here


if __name__ == "__main__":
    main()
