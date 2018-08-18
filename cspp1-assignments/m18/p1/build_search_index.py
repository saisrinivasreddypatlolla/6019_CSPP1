'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
FILENAME = "stopwords.txt"
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    temp2 = []
    characters = ".,';"
    for char in characters:
        if char in text:
            text = text.replace(char, '')


    temp1 = text.lower().split()
    temp2 = list(temp1)
    #print(temp2)
    for word in temp2:
        if word in load_stopwords(FILENAME):
            temp1.remove(word)


        #temp1.append(re.sub('[^a-zA-Z]','',word))

    #temp1 = []
    #temp1.append(re.sub('[^a-zA-Z]','',text))
    # characters ="!@#$%^&*()_+':;?012346789*/-+"
    #print(temp1)
    # for word in text:
    #     for character in characters:
    #         if character in word:
    #             word.replace(character, '')
    # print(text)
    return temp1

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    search_index = {}
    #print(docs)
    for line in range(len(docs)):
        updated_docs = word_list(docs[line])
        for word in updated_docs:
            if word not in search_index.keys():
                search_index[word] = [(line, updated_docs.count(word))]
            else:
                if (line, updated_docs.count(word)) not in search_index[word]:
                    search_index[word].append((line, updated_docs.count(word)))

    # for word in search_index:
    #     search_index[word] = set(search_index[word])

        #print(str1)
        #return str1.index(line)
    #print(search_index)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    return search_index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    #print(documents)
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
