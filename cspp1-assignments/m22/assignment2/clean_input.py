'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    list1 = string.split()
    characters = "!@#$%^&*()."
    list2 = []
    for word in list1:
        #print(char)
        for char in characters:
            if char in word:
                word = word.replace(char, '')
        list2.append(word)
    return ''.join(list2)

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
