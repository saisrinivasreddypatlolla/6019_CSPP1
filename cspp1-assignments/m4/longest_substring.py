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
