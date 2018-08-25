'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''This function is used to print the sorted order of given words with #*frequency'''
    sort_list = sorted(dictionary.keys())
    for word in sort_list:
        print(word, "-", '#'*dictionary[word])

def main():
    '''This function take dictionary as input and calls frequency graph function'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
