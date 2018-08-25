'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
from collections import Counter
def tokenize(string):
    list2 =[]
    list1 = []
    characters = '";.,'
    for word in string:
        #print(char)
        for char in characters:
            if char in word:
                word = word.replace(char, '')
        list1.append(word)
    # print(list1.split())

    counter = {}
    for line in list1:
        list2.append(line.split())
    print(list2)
    for line in list2:
        for word in line:
            if word not in counter.keys():
                counter[word] = 0
            counter[word] += 1
    return counter
            
def main():
    list1 = []
    number = int(input())
    for _ in range(number):
        string = input()
        list1.append(string)
    print(tokenize(list1))



if __name__ == '__main__':
    main()
