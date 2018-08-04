'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    this program is used to print the special caracters with " ".
    '''
    str_input = input()
    str_valb = "!@#$%^&*"
    str_val = ""
    for char in str_input:
        if char in str_valb:
            str_val = str_val+" "
        else:
            str_val = str_val+char
    print(str_val)
if __name__ == "__main__":
    main()
