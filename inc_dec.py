def increment(x):
    if type(x) not in [int, float]:
        raise TypeError('Input should be of numeric value')
    return x + 1

def decrement(x):
    return x - 1