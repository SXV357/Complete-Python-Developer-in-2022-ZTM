import re
import math

# #Q1
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

# Q2


def factorial(n):
    fact = 1
    for x in range(1, n + 1):
        fact *= x
    return fact


print(factorial(8))

# Q3


def dict_integral(n):
    for y in range(1, n + 1):
        yield y, y ** 2


print(dict(dict_integral(8)))

# Q4
new_input = input().split(',')
print(new_input)
print(tuple(new_input))

# Q5


class NewClass():
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def printString(self):
        print(self.string.upper())


new_str = NewClass('hello')
print(new_str.printString())

# Q6
user_input = input('Enter a set of numbers: ').split(',')
d = list(map(int, user_input))
c = 50
h = 30


def calc_root():
    res = []
    for i in range(len(d)):
        res.append(math.floor(math.sqrt((2 * c * d[i]) / h)))
    return res


print(calc_root())

# Q7


def generate_2D_array(x, y):
    return [[i * j for j in range(y)] for i in range(x)]


print(generate_2D_array(3, 5))

# Q8
new_input = input('Enter some words: ').split(',')
new_input.sort(key=lambda x: x[0])
print(','.join(new_input))

# Q9
print([i.upper() for i in input('Enter some words: ').split(',')])

# Q10
some_input = input('Enter some words again: ').split()
print(sorted(list(set(some_input))))

# Q11
binary_input = input('Enter a series of binary numbers: ').split(',')
decimal_list = [int(i, 2) for i in binary_input]
for index, value in enumerate(decimal_list):
    if value % 5 == 0:
        print(bin(value))

# Q12
for i in range(1000, 3001):
    str_version = str(i)
    if int(str_version[0]) % 2 == 0 and int(str_version[1]) % 2 == 0 and int(str_version[2]) % 2 == 0 and int(str_version[3]) % 2 == 0:
        print(i)

# Q13
inp = input('Enter a sentence: ').split()
num_letters = 0
num_digits = 0

for item in inp:
    for letter in item:
        if letter.isalpha():
            num_letters += 1
        elif letter.isdigit():
            num_digits += 1

print(f'LETTERS {num_letters}\nDIGITS {num_digits}')

# Q14
us_inp = input('Enter a sentence: ').split()
num_upper = 0
num_lower = 0

for word in us_inp:
    for char in word:
        if char.isupper():
            num_upper += 1
        elif char.islower():
            num_lower += 1

print(f'UPPER CASE {num_upper}\nLOWER CASE {num_lower}')

# Q15

inpu = input('Enter a number: ')

print(int(inpu) + int(inpu * 2) + int(inpu * 3) + int(inpu * 4))

# Q16
take_data = input('Enter some numbers: ').split(',')
int_list = list(map(int, take_data))
new_list = [i ** 2 for i in int_list if i % 2 != 0]
for item in new_list:
    print(''.join(str(item)))

# Q17
bank_transactions = input('Enter some transaction: ').split(',')
# ['D 300', 'D 300', 'W 200', 'D 100']


def calc_net_amount(li):
    net_amount = 0
    for i in li:
        if i[0] == 'D':
            net_amount += int(i[2:])
        elif i[0] == 'W':
            net_amount -= int(i[2:])
    return net_amount


print(calc_net_amount(bank_transactions))

# Q18
password = input('Enter a series of passwords: ').split(',')
for item in range(len(password)):
    if re.fullmatch('^[a-zA-Z0-9$#@]{6,12}$', password[item]):
        print(password[item])

# Q19
new_li = []
get_tuples = input().split(',')
for item in get_tuples:
    new_li.append(tuple(item))

new_li.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(new_li)

# Q20


class DivisibleBySeven():
    def isDivisible(self, num):
        for i in range(1, num + 1):
            if i % 7 == 0:
                yield i


for i in DivisibleBySeven().isDivisible(21):
    print(i)

# Q21
origin = list((0, 0))
x, y = 0, 0
up = int(input('How many steps up? '))
y += up
down = int(input('How many steps down? '))
y -= down
left = int(input('How many steps left? '))
x -= left
right = int(input('How many steps right? '))
x += right

total_dist = math.sqrt((y - origin[1]) ** 2 + (x - origin[0]) ** 2)
print(f'Total distance: {math.floor(total_dist)}')

# Q22


def frequency_of_words_in_sentence(sentence):
    word_list = sentence.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


print(frequency_of_words_in_sentence(
    'New to python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'))

# Q23


def calc_square(num, power):
    return num ** power


print(calc_square(2, 2))

# Q24


def int_to_string(number):
    print(str(number))

# Q25


def compute_sum(n1, n2):
    print(int(n1) + int(n2))

# Q26


def concatenate_strings(str1, str2):
    return str1 + str2

# Q27


def check_lens(s1, s2):
    if len(s1) == len(s2):
        print(s1, s2)
    elif len(s1) > len(s2):
        print(s1)
    elif len(s1) < len(s2):
        print(s2)

# Q28


def print_dict():
    return {i: i ** 2 for i in range(1, 21)}

# Q29


def only_keys():
    return {i: i ** 2 for i in range(1, 21)}.keys()

# Q30


def gen_list():
    return [i ** 2 for i in range(1, 21)]


# Q31
lis = [i ** 2 for i in range(1, 21)]
for i in range(0, 5):
    print(lis[i])

# Q32
new_lis = [i ** 2 for i in range(1, 21)]
print(new_lis[-5:])

# Q33
new_lis2 = [i ** 2 for i in range(1, 21)]
print(new_lis2[5:])

# Q34
some_list = [i ** 2 for i in range(1, 21)]
print(tuple(some_list))

# Q35


def get_first_and_second_half(tup):
    return tup[:int(len(tup) / 2)], tup[int(len(tup) / 2):]


print(get_first_and_second_half((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# Q36


def get_evens(tupl):
    return tuple(i for i in tupl if i % 2 == 0)


print(get_evens((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# Q37
str_inp = input('Enter a string: ')
if str_inp == 'yes' or str_inp == 'YES':
    print("Yes")
else:
    print("No")

# Q38


def square(i):
    return i ** 2


print(list(map(square, list(range(11)))))

# Q39


def new_sq(item):
    return item ** 2


sum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_list = list(map(new_sq, sum_list))


def divByTwo(i):
    return i % 2 == 0


print(list(filter(divByTwo, squares_list)))

# Q40
print(list(filter(lambda i: i % 2 == 0, list(range(0, 21)))))

# Q41
print(list(map(lambda x: x ** 2, list(range(1, 21)))))

# Q42


class American():
    def __init__(self, nationality):
        self.nationality = nationality

    @staticmethod
    def printNationality():
        print('I am an American')


united_states = American('American')
print(American.printNationality())

# Q43


class NewAmerican():
    pass


class NewYorker(NewAmerican):
    pass


united_states2 = NewAmerican()
new_yorker = NewYorker()
print(united_states2, new_yorker)

# Q44


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)


new_circle = Circle(5)
print(new_circle.calc_area())

# Q45


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width


new_rect = Rectangle(10, 5)
print(new_rect.compute_area())

# Q46


class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length ** 2


new_sq = Square(5)
print(new_sq.area())

# Q47
raise RuntimeError('This is a runtime error')

# Q48
try:
    print(5 / 0)
except ZeroDivisionError:
    print('Division by zero is not possible')

# Q49


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


new_exception = CustomException('This is a custom exception')
raise new_exception

# Q50
email = input('Enter an email: ')


def only_username(e):
    return e.split('@')[0]


print(only_username(email))

# Q51
new_email = input('Enter another email: ')


def only_company_name(new_e):
    return new_e.split('@')[1]


print(only_company_name(new_email))

# Q52
seq_words = input('Enter a sequence of words: ').split()
dig_list = []
for i in seq_words:
    if i.isdigit():
        dig_list.append(i)
print(dig_list)

# Q53
ascii_string = ascii(input('Enter a string: '))


def unicode_string_encoded_by_utf_8(asc):
    return asc.encode('utf-8')


print(unicode_string_encoded_by_utf_8(ascii_string))

# Q54
n = int(input('Enter the number: '))
total = 0
for i in range(1, n + 1):
    total += i / i + 1

print(round(total, 2))

# Q55
new_n = input('Enter some number: ')


def compute_value(x):
    if x == 0:
        return 0
    else:
        return compute_value(x - 1) + 100


print(compute_value(new_n))

# Q56
spec_term = int(input('Enter which term you want to compute: '))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n) - fibonacci(n - 1)


print(fibonacci(spec_term))

# Q57
new_spec_term = int(
    input('Enter how many fibonacci numbers you want to compute: '))
fib_list = [fibonacci(i) for i in range(new_spec_term + 1)]
print(','.join(str(i) for i in fib_list))

# Q58

new_inp = int(input('Enter the number: '))


def only_even(num):
    for i in range(0, num + 1):
        if i % 2 == 0:
            yield i


for x in only_even(new_inp):
    print(x)

# Q58
new_inp2 = int(input('Another number: '))


def byFiveAndSeven(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


arr = []
for y in byFiveAndSeven(new_inp2):
    arr.append(str(i))
print(','.join(arr))

# Q59


def only_evens(li):
    for i in len(range(li)):
        assert li[i] % 2 == 0
    print('All even numbers')


only_evens([2, 4, 6, 8])

# Q60

math_exp = input('Enter a mathematical expression: ')
solve = math_exp.split()


def get_answer(expression):
    n1 = expression[0]
    operation = expression[1]
    n2 = expression[2]
    if operation == '+':
        print(int(n1) + int(n2))
    elif operation == '-':
        print(int(n1) - int(n2))
    elif operation == 'x':
        print(int(n1) * int(n2))
    elif operation == '/':
        print(int(n1) / int(n2))
    else:
        print('You can only perform addition, subtraction, multiplication, or division')


get_answer(solve)
