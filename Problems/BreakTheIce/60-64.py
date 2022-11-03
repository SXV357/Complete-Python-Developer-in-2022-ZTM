import sys
import random

# 60
arg = int(sys.argv[1])
def compute_value(n):
    if n == 0:
        return n
    else:
        return compute_value(n-1) + 100

#61
new_arg = int(sys.argv[1])
def compute_fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return compute_fibonacci(n-1) + compute_fibonacci(n-2)

#62
def print_fibonacci(n):
    fib_list = []
    for i in range(n):
        fib_list.append(compute_fibonacci(i))
    print(fib_list)

#63
def generate_nums(n):
    vals = [str(i) for i in range(n) if i % 2 == 0]
    return ','.join(vals)

#64
def create(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

    nums_li = []
    for i in create(100):
        nums_li.append(str(i))
    return ''.join(nums_li)

#65
def generate_evens():
    return [random.choice(i) for i in range(0, 11) if i % 2 == 0]

#66
def generate_odds():
    return random.choice([x for x in range(10, 151) if x % 5 == 0 and x % 7 == 0])

#67
def gen_random(low, max):
    for i in range(low, max + 1):
        return random.sample(i, 5)

#68
def gen_even_random(l, m):
    for i in range(l, m + 1):
        if i % 2 == 0:
            return random.sample(i, 5)

#69
def gen_list():
    return random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5)