# Write a Python function that takes a string as an argument and prints whether it is upper or lowercase
def PrintCase(string):
    '''Discovering if provided string is upper or lower case.'''
    if string.islower() == True:
        print(f"{string} is lowercase.")
    elif string.isupper() == True:
        print(f"{string} is uppercase.")
    else:
        print(f"{string} is mixed case.")

PrintCase("James")
