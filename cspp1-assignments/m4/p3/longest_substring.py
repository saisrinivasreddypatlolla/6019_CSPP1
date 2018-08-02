'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    """This program is used to print longest alphabetical sequence to the given string"""
    str_val = input()
    end_val = 0
    count_valb = 0
    count_val = 0
    for char_val in range(len(str_val)-1):
        if str_val[char_val] <= str_val[char_val+1]:
            count_val += 1
            if count_val > count_valb:
                count_valb = count_val
                end_val = char_val+1
        else:
            count_val = 0
    str_vala = end_val - count_valb
    print(str_val[str_vala:end_val+1])
if __name__ == "__main__":
    main()
