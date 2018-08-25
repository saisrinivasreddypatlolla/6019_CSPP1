'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''This function is used to print the sorted order of given words with frequency'''
    sort_list = sorted(dictionary.keys())
    for word in sort_list:
        print(word, "-", dictionary[word])

def main():
    '''This function take dictionary as input and calls print dictionary function'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
