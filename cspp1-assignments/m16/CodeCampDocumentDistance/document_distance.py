'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILENAME = 'stopwords.txt'

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary_one = {}
    dictionary_two = {}
    characters = "'.,?!;:()-3"
    for character in characters:
        if character in dict1 or character in dict2:
            dict1 = dict1.replace(character, '')
            dict2 = dict2.replace(character, '')
    #print(dict2,dict1)
    list_of_words_inputone = []
    list_of_words_inputtwo = []
    # list3 = []
    # list4 = []
    frequency_words = {}
    list_of_words_inputone = dict1.lower().split()
    list_of_words_inputtwo = dict2.lower().split()
    # temp2 = []
    #print(list_of_words_inputone,list_of_words_inputtwo)
    # print(load_stopwords(FILENAME))
    # temp = "Wouldn't you like to be able to park like this young girl".split(" ")
    # for i in temp:
    #     if i in load_stopwords(FILENAME).keys():
    #         print("here =  ", i)
    #         temp.remove(i)
    #     else:
    #         temp2.append(i)
    # print(temp2)
    temporary_list_one = list(list_of_words_inputone)
    #temporary_list_one = list_of_words_inputone[:]
    temporary_list_two = list(list_of_words_inputtwo)
    # print(temporary_list_one)
    # print(temporary_list_two)
    for word in temporary_list_one:
        if word in load_stopwords(FILENAME) and word:
            list_of_words_inputone.remove(word)
            #instead of len(word) > 0 i wrote word
    for word in temporary_list_two:
        if word in load_stopwords(FILENAME) and word:
            list_of_words_inputtwo.remove(word)
            #instead of len(word) > 0 i wrote word
    #print(list_of_words_inputone)
    #print(list_of_words_inputtwo)
    for word in list_of_words_inputone:
        if word not in dictionary_one:
            dictionary_one[word] = list_of_words_inputone.count(word)
    for word in list_of_words_inputtwo:
        if word not in dictionary_two:
            dictionary_two[word] = list_of_words_inputtwo.count(word)
    keys = set(list(dictionary_one.keys())+list(dictionary_two.keys()))
    frequency_words = {key:[0, 0] for key in keys}
    #print(dictionary_one,dictionary_two)
    for key in dictionary_one:
        frequency_words[key][0] = dictionary_one[key]
    for key in dictionary_two:
        frequency_words[key][1] = dictionary_two[key]
    #print(frequency_words)
    sum_of_numerator = 0
    sum_first = 0
    sum_second = 0
    for keys in frequency_words.values():
        sum_of_numerator += keys[0]*keys[1]
        sum_first += keys[0]**2
        sum_second += keys[1]**2
    frequency = sum_of_numerator/(math.sqrt(sum_first)*(math.sqrt(sum_second)))
    return frequency

    #print(frequency_words)
    #print(list_of_words_inputone,list_of_words_inputtwo)
    # for word in list1:
    #   if char in word:
    #       #word1 = word.strip(char)
    #       list1 = list1.append(word.strip(char))
    # print(list1)


def load_stopwords(file):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords
#print(load_stopwords(filename))
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
