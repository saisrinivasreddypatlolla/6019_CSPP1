'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	''' this program is used to print the bob count in a given string'''
	STR = input("enter string ")
    COUNT = 0
    for I in range(len(STR) - 2):
    	if STR[I] == 'b' and STR[I+1] == 'o' and STR[I+2] == 'b':
        	COUNT += 1
	print(COUNT)
if __name__== "__main__":
	main()
