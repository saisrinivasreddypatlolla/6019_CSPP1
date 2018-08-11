'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    temp_list_one = []
    key_in_dictionary = []
    values_in_dictionaries = []
    dictionary = {}
    temp_list_two = []
    if len(data) < 20:
        return dictionary
    input_string = data.splitlines()
    for followers in input_string:
        temp_list_one.append(followers.split(" follows "))
    for following in temp_list_one:
        for index_of_follwing in range(len(following)):
            temp_list_two.append(following[index_of_follwing].split(','))

    for index_of_list in range(0, len(temp_list_two), 2):
        key_in_dictionary = temp_list_two[index_of_list]
        values_in_dictionaries = temp_list_two[index_of_list+1]
        if key_in_dictionary[0] in dictionary.keys():
            dictionary[key_in_dictionary].append(values_in_dictionaries)
        else:
            dictionary[key_in_dictionary[0]] = values_in_dictionaries
    return dictionary



def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
