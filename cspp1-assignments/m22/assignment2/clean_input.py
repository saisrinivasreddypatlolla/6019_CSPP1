'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''This method used to clean up the strings'''
    list_ofwords = string.split()
    characters = "!@#$%^&*()."
    cleaned_words = []
    for word in list_ofwords:
        #print(char)
        for char in characters:
            if char in word:
                word = word.replace(char, '')
        cleaned_words.append(word)
    return ''.join(cleaned_words)

def main():
    ''' This main function used to print the string without non alphabets
        from the given input.'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
