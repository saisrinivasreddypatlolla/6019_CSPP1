#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    key_value = []
    for key in aDict.keys():
        length_key = len(aDict[key])
        if length_key >= count:
            count = length_key
            key_value += [key]
    return key_value



def main():
    '''
    Main function for the given program
    '''
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(biggest(aDict))


if __name__== "__main__":
    main()