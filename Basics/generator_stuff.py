from time import time
# generators can generate values without taking up much memory space

range(100) # creates values one by one
list(range(100)) # creates list of 100 items in memory

def create_list(n):
    res = []
    for i in range(n):
        res.append(i ** 2)
    return res

print(create_list(101))

#all generators are iterable but not all iterables are generators

def generator_func(num):
    for i in range(num):
        yield i # pauses the function momentarily and returns a certain value
                # then loops over again and does the same thing until it reaches the end
                # stops function and returns back to iteration when next() is called

for item in generator_func(100): # generator is iterable
    print(item)

gen_item = generator_func(100)
# print(gen_item) # gen_item is a generator object
next(gen_item) # yields 0(can call this as many times as you want until range expires)
next(gen_item) # yields 1
print(next(gen_item)) # yields 2

#################################################################

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'Took {t2 - t1} seconds')
        return fn(*args, **kwargs)
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(10000000):
        i * 5

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i * 5

long_time()
long_time2()

############################################################
def special_for(iterable):
    iterator = iter(iterable) # converting list into iterable
    while True:
        try:
            print(iterator) # location of item in memory
            print(next(iterator)) # actual value of item
        except StopIteration: # loop till no more elements left to iterate over in iterable
            break

special_for([1, 2, 3, 4, 5])
#when list is passed in, it is converted into iterable and the next(i) is called for each
# item until there's no more items to iterate over and we break out of the loop

##############################################################

class MyGen():
    curr = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.curr < self.last: # is 0 < last number passed in
            number = MyGen.curr # current number = 0
            MyGen.curr += 1 # incrementing it by 1
            return number # returning final number after each iteration
        raise StopIteration('No more items to loop over') # stops looping once last elem has been reached

newGen = MyGen(0, 101)
for item in newGen:
    print(item ** 3)

#################################################

def fibonacci(num):
    n1, n2 = 0, 1
    for x in range(num):
        yield n1
        n1, n2 = n2, n1 + n2

for i in fibonacci(20):
    print(i)