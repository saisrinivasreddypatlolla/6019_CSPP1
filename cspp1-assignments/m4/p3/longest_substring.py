'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
	"""This program is used to print longest alphabetical sequence to the given string"""
	STR = input("enter string ")
	S = 0
	COUNT1 = 0
	COUNT = 0
	for i in range(len(STR)-1):
    	if STR[i] <= STR[i+1]:
        	COUNT += 1
        	if COUNT > COUNT1:
            	COUNT1 = COUNT
            	S = i+1
    	else:
        	COUNT = 0
	STR1 = S - COUNT1
	print(STR[STR1:S+1])
if __name__ == "__main__":
	main()
