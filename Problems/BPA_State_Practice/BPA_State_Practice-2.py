from fractions import Fraction
from functools import reduce

#1
# Notes
    # --> 1 x 1 = 1
    # --> 11 x 11 = 121
    # Formula = (10^2 - 1) / 9  (Equals 1, 11, 111, 1111, 11111 for each iteration)
    # Square the above to get each answer

def palindromic_triangle(N):
    # Solution 1
    arr = [str(i) for i in range(1, N + 1)]
    for i in range(1, N + 1):
        if i == 1:
            print(i, end = "\n")
        else:
            first = arr[0:i - 1]
            second = reversed(first)
            print(''.join(first) + str(i) + ''.join(second), end = "\n")

     #Alternate solution
    for i in range(1, N + 1):
        print((int(i * str(1))) * (int(i * str(1))), end = "\n")        

#2

# Notes
    # --> complex() converts a pair of numbers into a real and complex part
    # --> Operations can be performed by default but the result will now store 2 numbers
    # --> Calling the class(Complex) and passing in the real and imaginary values of
          # the result will invoke the __str__ method which prints out all the answers

import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    # Both require individual pairs to be added so no need to call complex() on each
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    def __mul__(self, no):
        product = complex(self.real, self.imaginary) * complex(no.real, no.imaginary)
        return Complex(product.real, product.imag) # calling class to invoke the string rep method
    def __truediv__(self, no):
        res = complex(self.real, self.imaginary) / complex(no.real, no.imaginary)
        return Complex(res.real, res.imag)
    def mod(self):
        return "%.2f+0.00i" % (math.sqrt(math.pow(self.real, 2) + math.pow(self.imaginary, 2)))
    # String representation of the output
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

def run_complex():
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c) # unpack all the values in the input
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    # calling the class' __str__ method on each of the operations
    # *map calls the string method on all the given pairs and what operation is performed

#3

# n = Num athletes = 5
# m = Num attributes = 3(rank, age, height)
# arr = [[], [], [], [], []] --> each subarray contains the attributes for each athlete
# k = what attribute to sort based on

def sort_athletes(n, m, arr, k):
    modified = sorted(arr, key = lambda x: x[k])
    for i in range(len(modified)):
        for j in range(len(modified[i])):
            modified[i][j] = str(modified[i][j])
    for sub_arr in modified:
        print(' '.join(sub_arr), end = "\n")

def run_sort_athletes():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sort_athletes(n, m, arr, k)

#4

#Conditions
    # All sorted lowercase letters are ahead of uppercase letters.
    # All sorted uppercase letters are ahead of digits.
    # All sorted odd digits are ahead of sorted even digits.

def sort_string():
    string = str(input())
    letters = []
    upper_case = []
    digits = []
    for i in range(len(string)):
        if string[i].isalpha():
            if not string[i].isupper():
                letters.append(string[i])
            else:
                upper_case.append(string[i])
        elif string[i].isdigit():
            digits.append(string[i])
    modified_lower = sorted(letters, key = lambda x: ord(x), reverse=False)
    modified_upper = sorted(upper_case, key = lambda y: ord(y), reverse = False)
    sorted_odd = sorted([str(int(val)) for val in digits if int(val) % 2 != 0])
    sorted_even = sorted([str(int(val)) for val in digits if int(val) % 2 == 0])
    joined_letters = ''.join(modified_lower) + ''.join(modified_upper)
    joined_nums = ''.join(sorted_odd) + ''.join(sorted_even)
    print(joined_letters + joined_nums)

# sort_string()

#5
def validate_email(string):
    if "@" in string and "." in string and string[string.index(".") + 1:len(string)]:
        rate = string.index("@")
        period = string.index(".")
        username = string[0:rate]
        website = string[rate + 1:period]
        extension = string[period + 1:len(string)]
        lower_case = [str(chr(i)) for i in range(97, 123)]
        upper_case = [str(j).upper() for j in lower_case]
        nums = [str(val) for val in range(0, 10)]
        symbols = ["-", "_"]
        res1 = False
        for x in range(len(username)):
            if username[x] in lower_case or username[x] in upper_case or username[x] in nums or username[x] in symbols:
                res1 = True
            else:
                res1 = False
        res2 = False
        for y in range(len(website)):
            if website[y] in lower_case or website[y] in upper_case or website[y] in nums:
                res2 = True
            else:
                res2 = False
        res3 = False
        for z in range(len(extension)):
            if extension[z] in lower_case or extension[z] in upper_case:
                res3 = True
            else:
                res3 = False
        return res1 and res2 and res3 and len(extension) == 3
    else:
        return False

def filter_mail(emails):
    return list(filter(validate_email, emails))

def run_email_filtering():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

#6
def product(fracs):
    t = Fraction(reduce(lambda x, y: x * y, fracs))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
