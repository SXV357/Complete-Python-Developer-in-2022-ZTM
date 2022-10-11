import pdb

def some_func(n1, n2):
    pdb.set_trace() # stops here and allows you to test your code to figure out errors(step through and debug)
    return n1 ** n2

some_func(2, 'ahdjfqfif')
# pdb.runcall(some_func, 2, 'ajgafsgjf') returns whatever function call returned