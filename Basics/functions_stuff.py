def calc_pow(a = 2, b = 5): # default parameters
    return a ** b

print(calc_pow(3, 6))
# keyword arguments(specify which values for args)
print(calc_pow(a = 5, b = 7))
# if function is called w/o arguments default params will be used
print(calc_pow())

#nested functions
def func(x, y):
    def new_func(x1, y1):
        return int(x1 / y1)
    return new_func(x, y)
   
print(func(10, 5))



def checkDriverAge(age = 0):
    if age < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif age > 18:
        print("Powering On. Enjoy the ride!")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(age = 92)

#docstrings

def new_func(x, y):
    '''
    This function adds two numbers
    '''
    return x + y

help(new_func) # can be used to get info about purpose of function
print(new_func.__doc__)

# *args and **kwargs can be used when wanting to pass a variable number of arguments into a function

def add_nums(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(kwargs.values()) # kwargs stores arguments in a dictionary format

print(add_nums(1, 2, 3, 4, 5, n1 = 1, n2 = 2, n3 = 3)) # specifying args and then kwargs
#rule for parameters: parameters, *args, default parameters, **kwargs

def highest_even(li):
    even_number_list = []
    for i in li:
        if i % 2 == 0:
            even_number_list.append(i)
    return max(even_number_list)

print(f'The highest even number is {highest_even([10, 2, 3, 4, 8, 11])}')

