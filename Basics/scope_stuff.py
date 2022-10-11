# scope

some_var = 5 # global variable(has global scope)

def some_func():
    some_var = 10 # local variable(has local scope)
    print("{} has local scope(function scope)".format(some_var))

some_func()
print(some_var) # will return 5 and not 10 because 10 isn't a global variable

#rules for checking scope
#1 - local scope
#2 - parent function scope
#3 - global scope
#4 - built-in function scope

def parent_func():
    some_var = 25 # (since this is removed, interpreter checks global scope and some_var = 5 which is returned)
    def child_func():
        return some_var
    return child_func()

print(parent_func()) # checks local first, and then parent, so once it finds 25, it returns 25
print(some_var)



#accessing global variables from a function
global_var = 10

def function():
    global global_var #defining it before accessing it(if not defined, error will be thrown)
    global_var -= 5 # for making changes to a global variable within the local scope
    return global_var

def new_function(global_var):
    global_var -= 5
    return global_var

print(function())
print(new_function(global_var))



def outer():
    x = "local" # parent local scope
    def inner():
        nonlocal x # nonlocal keyword modifies outer scope because it is no longer a local variable
        x = "nonlocal"
        print("inner:", x) # nonlocal
    inner()
    print("outer:", x) # nonlocal(exisiting local variable in parent scope is changed instead of 
    #creating a new variable)

outer()