# Use fire to access methods in an existing Python script from the command line
#A bit fiddly in PS, on the command line type "python %scriptname%.py greet arg1 arg2 OR goodbye arg1 arg2"
import fire

def greet(greeting='Salve amice,', name='James'):
    print(f"{greeting} {name}")

def goodbye(goodbye='Et tu,', name='James?'):
    print(f"{goodbye} {name}")

if __name__ == '__main__':
    fire.Fire()