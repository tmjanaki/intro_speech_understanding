'''
This homework defines one method, called "arithmetic".
that method, type `help homework2.arithmetic`.
'''

def arithmetic(x, y):
    if isinstance(y, str):
        if isinstance(x, str):
            return x + y
        elif isinstance(x, float):
            return str(x) + y

    elif isinstance(y, float):
        if isinstance(x, str):
            return x * int(y)
        elif isinstance(x, float):
            return x * y

    return 0


