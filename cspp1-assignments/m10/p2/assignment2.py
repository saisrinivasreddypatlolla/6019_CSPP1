'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    index=0
    if lettersGuessed[index] in secretWord:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temporary_list = []
    for letters_in_list in secretWord:
        if letters_in_list in lettersGuessed:
            temporary_list.append(letters_in_list)
        else:
            temporary_list.append('_')
    return ''.join(temporary_list)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = "abcdefghijklmnopqrstuvwxyz"
    string = list(string)
    for letters_in_string in lettersGuessed:
        if letters_in_string in lettersGuessed:
            string.remove(letters_in_string)
    return ''.join(string)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("welcome to the game, hangman!")
    print("Iam thinking of a word that is:",str(len(secretWord)),"long")
    lettersGuessed = []
    guess_chances = 8
    win_flag = 0
    while(guess_chances > 0 and win_flag == 0):
        print("-------------------------------------------------------------------")
        print("you have", str(guess_chances),"left")
        print("available letters:", getAvailableLetters(lettersGuessed))
        guessed_letter = list(input("please enter a letter: "))
        if guessed_letter[0] in lettersGuessed:
        # print(guessed_letter)
        # print(lettersGuessed)
            print("Oops! you have already guessed that letter :", getGuessedWord(secretWord,lettersGuessed))
        else:
            lettersGuessed = lettersGuessed+guessed_letter
            if isWordGuessed(secretWord,guessed_letter) == True:
                print("good guess_chances", getGuessedWord(secretWord,lettersGuessed))
                if secretWord == getGuessedWord(secretWord,lettersGuessed):
                    win_flag = 1
            else:
                print("Oops! that letter is  not in my word:", getGuessedWord(secretWord,lettersGuessed))
                guess_chances -= 1
    if win_flag ==1:
        print("you won")
    else:
        print("sorry, you ran out of guesses, The word was:"+secretWord)






def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
