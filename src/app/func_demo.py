'''
Demo Functions
'''
def func(a: int,b: int) -> int:
    '''
    Docstring for func
    
    :param a: Description
    :param b: Description
    '''
    print("This is a function")
    return a + b

def sub(m: str,n: str) -> None:
    '''
    Function to just print the args
    
    :param m: int
    :param n: int

    Return None
    '''
    print(m,n)

if __name__ == '__main__':
    A = 10
    B = 100
    print(func(2,3))
    sub(2,4)
