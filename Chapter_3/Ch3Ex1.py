# Use sys to write a script that prints command line only when run from the command line.
def cmd_line():
    '''Defining the string "Command Line" to be printed'''
    message = 'Command Line'
    print(message)

'''Checking to see if script is run from command line'''
if __name__ == '__main__':
    cmd_line()