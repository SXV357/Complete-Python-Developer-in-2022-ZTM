class PlayerCharacter:

    relationship_status = "single" # class obj attribute(static and doesn't change)
    friends = ['x', 'y', 'z'] # class object attribute

    def __init__(self, name = "Jack Ryan", age = 35, email = "jack.ryan_211@gmail.com"): # constructor method
        if self.relationship_status == "single":
            self.name = name # instance attribute
            self.age = age
            self.email = email
        else:
            pass

    def run(self): # instance method
        print(f'My name is {self.name} and I\'m running right now!')
        return '' # need to return something

player1 = PlayerCharacter(name = "Shreyas", age = 17, email = "shrevis2018@gmail.com") # instantiating the class
player2 = PlayerCharacter(name = "Harshith", age = 13, email = "vishur@hotmail.com") # instantiating the class
player3 = PlayerCharacter() # will use default params since no args given

# has_friends = input("Does this player have friends? ")
# if has_friends == "yes":
#     for i in player1.friends: 
#         print(f'{player1.name} has a friend named {i}')
# else:
#     print(f'{player1.name} doesn\'t have any friends')

print(player1.run())
print(player2.run())

print(player3.name)
print(player3.age)
print(player3.email)

############################################################################################################

class Cat:
    species = 'mammal'
    is_pet = True
    def __init__(self, name, age, color):
        if self.is_pet:
            self.name = name
            self.age = age
            self.color = color
    
    @classmethod # can be accessed without instantiating the class()
    def calc_age(cls, n1 = 2, n2 = 3):
        return cls("Sally", n1 + n2, "orange") # instantiating the class using class method
    
    @staticmethod
    def common_items_in_two_lists(l1, l2): # completely self-isolated(can't access class or instance attributes)
        return set(l1).intersection(set(l2))

cat1 = Cat("Ryan", 12, "brown")
cat2 = Cat("Henry", 17, "white")
cat3 = Cat("Jack", 11, "black")
cat4 = Cat.calc_age(3, 5) # creating an object using class method(can directly call the function defined in the class method

def find_oldest_cat():
    oldest_cat = cat1.age
    for i in [cat1.age, cat2.age, cat3.age]:
        if i > oldest_cat:
            oldest_cat = i
    return oldest_cat

def check_color():
    for j in [cat1.color, cat2.color, cat3.color]:
        if j == "white" or j == "black":
            return True
        else:
            return False

print(f"The oldest cat is {find_oldest_cat()} years old.")
print(check_color())
print(cat4.name)
print(cat4.age)
print(cat4.color)
print(cat4.common_items_in_two_lists([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

############################################################################################################

class Car:
    comes_with_braking_system = True
    def __init__(self, age = "new", engine = "v9", horsepower = "575", mileage_per_year = 11200, zero_to_sixty = 3.125):
        if self.comes_with_braking_system: # class object attribute and refers to Car class
            self.age = age
            self.engine = engine
            self.horsepower = horsepower
            self.mileage_per_year = mileage_per_year
            self.zero_to_sixty = zero_to_sixty

    @classmethod
    def new_instance(cls, hp, mpy, zts):
        return cls("new", "v9", hp + 300, mpy * 3, zts / 3)

car1 = Car(age = "new", engine = "v8", horsepower = 500, mileage_per_year = 10000, zero_to_sixty = 3.5)
car2 = Car(age = "used", engine = "v6", horsepower = 300, mileage_per_year = 9200, zero_to_sixty = 2.5)
car3 = Car(age = "new", engine = "v12", horsepower = 600, mileage_per_year = 13500, zero_to_sixty = 2.1)
car4 = Car.new_instance(200, 4000, 10.2)

def check_mileage():
    for i in [car1.mileage_per_year, car2.mileage_per_year, car3.mileage_per_year, car4.mileage_per_year]:
        if int(i) > 12000:
            return f'{i} is too high. Keep it equal to or below 12000'
        else:
            return f'{i} is normal. Maintain it at that level.'

def max_hp():
    return f'The highest horsepower is {max([car1.horsepower, car2.horsepower, car3.horsepower, car4.horsepower])}'

print(check_mileage())
print(car4.age)
print(car4.engine)
print(car4.horsepower)
print(car4.mileage_per_year)
print(car4.zero_to_sixty)
print(max_hp())
