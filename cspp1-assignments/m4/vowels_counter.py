"""this program is used to print number of vowels occured in a given string"""
STR = input("enter string ")
COUNT = 0
for CHAR in STR:
    if CHAR in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1
print(COUNT)
