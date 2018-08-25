'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    '''This function is used to return the dictionary contains words and its occurance'''
    temporary_list2 = []
    temporary_list1 = []
    characters = '";.,'
    for word in string:
        for char in characters:
            if char in word:
                word = word.replace(char, '')
        temporary_list1.append(word)

    counter = {}
    for line in temporary_list1:
        temporary_list2.append(line.split())
    for line in temporary_list2:
        for word in line:
            if word not in counter.keys():
                counter[word] = 0
            counter[word] += 1
    return counter
def main():
    '''This main function print the dictionary which has words and its occurance
        in the given sentence'''
    list1 = []
    number = int(input())
    for _ in range(number):
        string = input()
        list1.append(string)
    print(tokenize(list1))



if __name__ == '__main__':
    main()
