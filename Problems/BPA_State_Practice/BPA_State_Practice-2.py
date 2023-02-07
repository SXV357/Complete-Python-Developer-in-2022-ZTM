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

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c) # unpack all the values in the input
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    # calling the class' __str__ method on each of the operations
    # *map calls the string method on all the given pairs and what operation is performed
