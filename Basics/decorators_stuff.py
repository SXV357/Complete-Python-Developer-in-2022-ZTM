from time import time
import math

def random_func():
    print('random_func')

new_var = random_func
del random_func # name reference is deleted but since another variable is pointing to function it still exists
print(new_var()) # when called "random_func" is printed even though location in memory has been deleted

#can also do this
def new_func(some_func): # this is a higher order function(it accepts another function)
    some_func()

def other_func():
    print('other_func')

print(new_func(other_func)) # the function acts as a variable in this case

#decorators provide extra functionality to functions
#example of another HOF
def func():
    def func2():
        return ' '
    return func2  # this is also a HOF since a function is being returned

#############################################################################################################

#basic structure of decorator function

def decorator_func(func):
    def wrapper_func(*args, **kwargs): # in order to call supercharged function with parameter, wrapper function needs parameter
        # to unpack all positional and keyword arguments
        print('*******************************************')
        func(*args, **kwargs)
        print('*******************************************')
    return wrapper_func

@decorator_func # used to call the decorator function
def something(): # im calling the decorator function here
    print('something')

@decorator_func
def something_else(param, param2, param3, param4):
    print(param, param2, param3, param4)

something_else([4,5,6], param2 = [7,8,9], param3 = [10,11,12], param4 = [13,14,15]) # just prints wrapper func on top and bottom

# something()

# decorator_func(something)() # will produce same output as above

# var = decorator_func(something)
# var() # will produce same output as above


###############################################################################################

#performance decorator

def performance(function):
    def wrapper(*args, **kwargs):
        t1 = time() # checks time at beginning of function
        function(*args, **kwargs)
        t2 = time() # checks time at end of function
        print(f'it took {round(t2-t1, 2)} seconds to run')
    return wrapper

@performance
def length_to_finish_loop():
    for i in range(10000000):
        i ** 5

length_to_finish_loop()


###############################################################################################

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'Name': 'Sorna',
    'is_valid': True
}

def authenticated(fn):
  def wrapper(dictionary):
    if dictionary['is_valid']:
        fn(dictionary)
    else:
        print("{} cannot be given access to this function.".format(dictionary['Name']))
  return wrapper

@authenticated
def message_friends(user):
    print('Message has been sent to {}'.format(user['Name']))

message_friends(user1)

###############################################################################################

def new_decorator(function):
    is_callable = True
    def wrapper_function(*args, **kwargs):
        print("Execution of the wrapper function")
        if is_callable:
            function(*args, **kwargs)
        else:
            print("No arguments passed. Cannot run this function")
    return wrapper_function

@new_decorator
def get_evens(list):
    return ['even' if i % 2 == 0 else 'odd' for i in list]

@new_decorator
def multiples_of_seven(list):
    return filter(lambda x: x % 7 == 0, list)

# print(tuple(get_evens(list(range(1001)))))
# print(tuple(multiples_of_seven(list(range(1001)))))


# new wrapper function
def new_dec(fn):
    def new_wrap(*args, **kwargs):
        fn(*args, **kwargs)
    return new_wrap

def get_square_roots(i):
    return round(math.sqrt(i), 3)

@new_dec
def return_diff_items(li):
    print(list(map(get_square_roots, li)))

new_li = list(range(1001))
return_diff_items(new_li)

