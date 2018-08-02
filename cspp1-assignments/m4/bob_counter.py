"""This program is used to print the bob counter"""
STR = input("enter string ")
COUNT = 0
for I in range(len(STR) - 2):
    if STR[I] == 'b' and STR[I+1] == 'o' and STR[I+2] == 'b':
        COUNT += 1
print(COUNT)
