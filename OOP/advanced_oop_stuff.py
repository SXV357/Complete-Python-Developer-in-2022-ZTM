class User():
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email) # can call init method of User class from the init method of wizard class
        # email needs to be passed in as a parameter in both areas in order for object to be able to access it 
        super().__init__(email) # alternate way of accessing email attribute(self no longer needed)
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1 = Wizard("New Wizard", 50, "new_wiz211@gmail.com")
print(wizard1.email) # thows an error because wizard class doesn't have access to email attribute(case 1)
#case 2: wizard object has access to init method of User class and email just needs to be passed in as an argument
print(dir(wizard1)) # check what methods and attributes are available to wizard1
print(help(wizard1))


################################################################################################

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'This toy\'s color is {self.color} and it is {self.age} years old'

    def __call__(self):
        return 'This toy is really cool!'

    def __getitem__(self, i):
        print(i, type(i))

    def __invert__(self):
        return self.color[::-1]

    def __len__(self):
        return len(self.color)

    def __pos__(self):
        return self.age + 1

new_toy = Toy("vanilla orange", 3)
print(new_toy.__str__()) # the dunder method can be modified(orginally returns strin representation of object)
print(str(new_toy)) # since __str__ method is modified, it will print out same result as before

print(new_toy()) # call method can be used when wanting to call object as a function

new_toy.__getitem__(1)
new_toy[{"k1": "v1", "k2": "v2"}] # can use indexing feature with __getitem__ method
print(new_toy.__invert__())
print(new_toy.__len__())
print(new_toy.__pos__())

################################################################################################

class SuperList(list): # list becomes parent class and all methods of list class are available to SuperList class
    def __len__(self):
        return 1000

super_list1 = SuperList()
print(super_list1.__len__())
n = 5
for i in range(n ** 3):
   if i % 2 == 0 and i % 3 == 0:
       super_list1.append(i)
print(super_list1[::-1])
print(isinstance(super_list1, list))
print(isinstance(super_list1, object))

################################################################################################

class ConvertIntegerToRoman():

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.convert_to_roman()
        
    def convert_to_roman(self):
        roman_numeral_map = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
        roman_numeral = ''
        for numeral, integer in roman_numeral_map:
            while self.number >= integer:
                roman_numeral += numeral
                self.number -= integer
        return roman_numeral

n1 = ConvertIntegerToRoman(478)
print(n1.convert_to_roman())

################################################################################################

class Rectangle():
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def calc_area(self):
        return self.l * self.w

cord1 = Rectangle(2, 3)
print(cord1.calc_area())

################################################################################################

class Circle():
    def __init__(self, diameter):
        self.diameter = diameter

    def calc_perimeter(self):
        radius = self.diameter / 2
        return 2 * radius * 3.14

    def calc_area(self):
        radius = self.diameter / 2
        return 3.14 * (radius ** 2)

c1 = Circle(44.57)
print(c1.calc_perimeter())
print(c1.calc_area())

################################################################################################

class String():
    def get_String(self):
        new_string = input('Enter a string: ')
        return new_string
    def print_String(self, new_string):
       print(new_string.upper())

user_input = String()
s1 = user_input.get_String()
user_input.print_String(s1)

################################################################################################

class EqualsTarget():
    
    def __init__(self, array, target):
        self._array = array
        self._target = target

    def check_indices(self, _array, _target):
        for i in range(len(self._array)):
            if self._array[i] + self._array[i + 1] == self._target:
                return f'1st index: {i}, 2nd index: {i + 1}'
        return 'No two numbers add up to the target'

check = EqualsTarget([30,20,15,40,10,20,70], 30)

print(check.check_indices(check._array, check._target))

################################################################################################

#multiple inheritance

class NewUser():
    def log_in(self):
        print('logged in')

class Wizard2():
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')
        return ''

class Archer2():
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    def arrows_rem(self):
        print(f'attacking with arrows of {self.arrows}')
        return ''

class Hybrid(Wizard2, Archer2):
    def __init__(self, name, power, arrows):
        Archer2.__init__(self, name, arrows) # getting access to instance method of archer class
        Wizard2.__init__(self, name, power) # getting access to instance method of wizard class

hb = Hybrid('Hybrid', 55, 10)
print(hb.attack())
print(hb.arrows_rem())

