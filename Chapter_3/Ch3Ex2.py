# Use click to create a command-line tool that takes a name as an argument and prints it if it does not begin with a p.
import click

'''Indicate that a function should be exposed to command line access & add arguments to the command-line 
    that link to the function paramaters of the same name (detail & name)'''
@click.command()
@click.option('--detail', default='Submitted name:', help='Text appearing before name')
@click.option('--name', default='James', help='Only names not beginning with "P" will be printed')

def name(detail, name):
    '''Don't print a name that starts with "P"'''
    result = name.startswith(('P', 'p'))
    if result == False:
        print(f"{detail} {name}")

'''Checking to see if script is run from command line'''
if __name__ == '__main__':
    name()