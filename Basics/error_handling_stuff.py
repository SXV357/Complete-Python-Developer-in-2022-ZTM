while True:
    try:
        age = int(input('What\'s your age? '))
        print(100 / age)
        # raise Exception('Only numbers allowed') --> can manually raise error/exception
    except ValueError:
        print("Only numbers allowed")
    except ZeroDivisionError:
        print("Cannot enter a zero")
    else: # works in conjunction w try statement(if exception, execute this, else do this)
        print("Thanks!")
        break
    finally: # will run no matter what(even after breaking out of loop)
        print("Finally done")
# can have as many except blocks as you want
# if 2 except blocks with same error specified, only first one will run if caught


def add_nums(n1, n2):
    try:
        return n1 + n2
    except TypeError as err:
        # can also wrap multiple errors --> except (error 1, error 2...) as err
        return f'Both values either need to be strings or numbers: {err}' #actually displaying the error

print(add_nums('1', 2))

############################################################

def isPrime():
    number = int(input('Enter a number: '))
    try:
        assert number > 0
    except AssertionError:
        print(f'{number} is not a positive number')
    else:
        for i in range(2, number):
            if number % i == 0:
                print(f'{number} is not a prime number')
            else:
                print(f'{number} is a prime number')

isPrime()