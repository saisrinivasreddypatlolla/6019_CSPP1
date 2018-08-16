'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def is_four_of_kind(hand):
    #value_list = high_values(hand)
    '''
        How do we find out if the given hand is a four of kind?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a four of kind
        Think of an algorithm: given the card suite how to check if it is a four of kind
        Write the code for it and return True if it is a four of kind else return False
    '''
    sorted_list = sorted(high_values(hand))
    set_sorted_list = set(sorted_list)
    if len(sorted_list) - len(set_sorted_list) == 3:
        return True
    return False
def is_three_of_kind(hand):
    '''
        How do we find out if the given hand is a three of kind?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a three of kind
        Think of an algorithm: given the card suite how to check if it is a three of kind
        Write the code for it and return True if it is a three of kind else return False
    '''
    value_list = sorted(high_values(hand))
    for i in range(len(value_list)-2):
        if value_list[i] == value_list[i+1] == value_list[i+2]:
            return True
    return False
def is_one_pair(hand):
    '''
        How do we find out if the given hand is a one pair?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a one pair
        Think of an algorithm: given the card suite how to check if it is a one pair
        Write the code for it and return True if it is a one pair else return False
    '''
    value_list = sorted(high_values(hand))
    set_sorted_list = set(value_list)
    if len(value_list)-len(set_sorted_list) == 1:
        return True
    return False
def is_two_pair(hand):
    '''
        How do we find out if the given hand is a two pair?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a two pair
        Think of an algorithm: given the card suite how to check if it is a two pair
        Write the code for it and return True if it is a two pair else return False
    '''
    value_list = sorted(high_values(hand))
    set_sorted_list = set(value_list)
    if len(value_list) - len(set_sorted_list) == 2:
        return True
    return False
def is_full_house(hand):
    '''
        How do we find out if the given hand is a full house?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a full house
        Think of an algorithm: given the card suite how to check if it is a full house
        Write the code for it and return True if it is a full house else return False
    '''
    value_list = sorted(high_values(hand))
    if (value_list[0] == value_list[1] == value_list[2]) and (value_list[3] == value_list[4]):
        return True
    if (value_list[0] == value_list[1]) and (value_list[2] == value_list[3] == value_list[4]):
        return True
    return False

def high_values(hand):
    '''
        How do we find high values of given hand?
        The hand has a list of cards represented as strings
        Do we need both carachters in the string? No.
        The first character is good enough to find high values
        Wrte the code for it and return list of face values of the given hand
    '''
    temporary_list_for_high_values = []
    for card_in_hand in hand:
        if card_in_hand[0] == 'A':
            temporary_list_for_high_values.append(14)
        elif card_in_hand[0] == 'K':
            temporary_list_for_high_values.append(13)
        elif card_in_hand[0] == 'Q':
            temporary_list_for_high_values.append(12)
        elif card_in_hand[0] == 'J':
            temporary_list_for_high_values.append(11)
        elif card_in_hand[0] == 'T':
            temporary_list_for_high_values.append(10)
        else:
            temporary_list_for_high_values.append(int(card_in_hand[0]))
    return temporary_list_for_high_values

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    value_list = sorted(high_values(hand))
    count = 0
    #print(hand)
    #sorted_hand = sorted(value_list)
    #print(sorted_hand)
    for i in range(len(value_list)-1):
        if value_list[i+1] - value_list[i] == 1:
            count += 1
    if count == len(value_list)-1:
        return True
    return False


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suite_of_card = hand[0][1]
    count = 1
    for card in range(1, len(hand)):
        if suite_of_card == hand[card][1]:
            count += 1
    if count == len(hand):
        return True
    return False
# def is_high_card(hand):
#     temporary_list_for_high_values = []
#     for card_in_hand in hand:
#         if card_in_hand[0] == 'A':
#             temporary_list_for_high_values.append(0.14)
#         elif card_in_hand[0] == 'K':
#             temporary_list_for_high_values.append(0.13)
#         elif card_in_hand[0] == 'Q':
#             temporary_list_for_high_values.append(0.12)
#         elif card_in_hand[0] == 'J':
#             temporary_list_for_high_values.append(0.11)
#         elif card_in_hand[0] == 'T':
#             temporary_list_for_high_values.append(0.10)
#         else:
#             temporary_list_for_high_values.append(float(card_in_hand[0])/100)
#         #print(temporary_list_for_high_values)
#     #temporary_list_for_high_values = sorted(temporary_list_for_high_values)
#     return max(temporary_list_for_high_values)
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_full_house(hand):
        return 7
    if is_two_pair(hand):
        return 2
    if is_one_pair(hand):
        return 1
    if is_three_of_kind(hand):
        return 3
    if is_four_of_kind(hand):
        return 4
    if is_flush(hand) and is_straight(hand):
        return 8
    if is_straight(hand):
        return 5
    if is_flush(hand):
        return 6
    return 0
    #return is_high_card(hand)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand

    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
