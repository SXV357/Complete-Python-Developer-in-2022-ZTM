import utility # importing another file to use in this program(file gets cached so no need to be compiled again)
# from Shopping import shopping_cart # importing a module from a package(import Shopping.shopping_cart) -> can also be done this way
from Shopping.shopping_cart import buy_something # importing a function from a module inside a package


if __name__ == '__main__':
    print(utility)
    print(utility.some_func(2, 3)) # can access functions defined in another file like this
    print(utility.another_func(2, 3))
    print(buy_something(20))

# ensure that only if module has name of main we're running it(file that is being run will have that name)
# if this is the file that gets run, do something

print(__name__) # each import command is run first at the beginning and saved in memory so interpreter
# has access to all methods and classes of that specific module