# # encapsulation - binding of attributes and methods into a single object that can be accessed by user
# # taking the functionality of the class and packaging it into a single object that has access to class attributes
# # and class/instance methods

# #abstraction - hiding implementation details from user via certain methods

# class SampleClass:
#     def __init__(self, name, age):
#         self._name = name #private attribute(shouldn't be modified or touched) - denoted by underscore
#         self._age = age

#     def say_something(self):
#         return f'Hello, my name is {self._name} and I\'m {self._age} years old'

# person1 = SampleClass("John", 16) # encapsulation(binding class functionality into an instance)
# person1.name = "Shreyas" # gets overwritten even though specified as a private variable
# print(person1.name)
# print(person1.say_something()) # we have access to this method but how its being implemented is hiddden from us

# ######################################################################################################

# class User():
#     def sign_in(self):
#         if self.check_age():
#             username = input("Enter username:")
#             password = input("Enter password:")
#             if username and password:
#                 print(f'Welcome {username}. You have successfully signed in.')
#             elif username and not password:
#                 print("Password cannot be empty.")
#             elif not username and password:
#                 print("Username cannot be empty.")
#             else:
#                 print("Sign in unsuccessful")
#         else:
#             print("You are not eligible to sign in. A parent account must be created")

#     def check_age(self):
#         age = int(input("Enter your age:"))
#         return age >= 18

#     def attack(self):
#         print("This attack is not implemented yet")

# class Wizard(User): # inheriting properties of User class so it has access to sign_in() method
#     has_special_powers = True
#     def __init__(self, name, power, health):
#         if self.has_special_powers:
#             self._name = name
#             self._power = power
#             self._health = health
#         else:
#             self.name = name
#             self.health = health

#     def attack(self):
#         User.attack(self) # passing User to wizard so to access parent method, self needs to be passed as argument
#         print(f'attacking with power of {self._power}')

# class Archer(User):

#     def __init__(self, name, num_arrows, health):
#         self._name = name
#         self._num_arrows = num_arrows
#         self._health = health

#     def attack(self):
#             print(f'Attacking with arrows. Arrows left --> {self._num_arrows - 1}')

# wizard1 = Wizard("Shreyas", 50, 100)
# archer1 = Archer("Someone", 35, 100)

# #check if wizard1 is an instance of parent class

# print(isinstance(wizard1, Wizard)) # --> True
# print(isinstance(wizard1, User)) # --> True

# # all instances inherit methods from object class

# print(isinstance(wizard1, object)) # --> True("object" is the parent class of all classes)

# def call_player_attacks(obj): # can also create a function to call the attack method of the player(polymorphism)
#     return obj.attack()

# call_player_attacks(wizard1) # both player objects have access to attack method but they perform different actions
# call_player_attacks(archer1)

# #alternate method to call both player attacks
# for i in [wizard1, archer1]:
#     i.attack()

# wizard1.attack() # can run attack method of Wizard class and of User class
# wizard1.sign_in()


# #########################################################################################################

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add another Cat
class Jerry(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
Cat1 = Simon("Simon", 2)
Cat2 = Sally("Sally", 5)
Cat3 = Jerry("Jerry", 1)
cats = [Cat1, Cat2, Cat3]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()