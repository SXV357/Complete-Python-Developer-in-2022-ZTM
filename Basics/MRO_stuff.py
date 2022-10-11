# class A():
#     num = 10 # if passed, error is thrown because num is not accessible in any class

# class B(A):
#     pass

# class C(A):
#     num = 1 # if passed, when calling D.num, 10 will be returned

# class D(B, C):
#     pass

# print(D.num)
# # since class B is passed first, it gets run and since nothing happens, it moves on to Class C
# # since class C inherits from class A, it originally has num = 10, but we're overwriting it with 1
# # so class D has an attribute num which is now equal to 1 and when we call it that's what we get

# print(D.__mro__) # returns order in which classes are checked in case of multiple inheritance

# class X: pass
# class Y: pass
# class Z: pass
# class A(X, Y): pass
# class B(Y, Z): pass
# class M(B, A, Z): pass

# print(M.__mro__)

###############################################################################################

# Q1
class Vehicle():
    def __init__(self, max_speed, mileage, color = "White"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        super().__init__(max_speed, mileage)

    def seating_capacity(self, capacity = 50):
        return f'The seating capacity of a {self.name} is {capacity} passengers'

    def fare(self, capacity = 50):
        tax = (10 / 100) + 1
        return capacity * 100 * tax

class Car(Vehicle):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        super().__init__(max_speed, mileage)


new_bus = Bus("School Volvo", 180, 12)
new_car = Car("Audi Q5", 240, 18)
print(f'Color: {new_bus.color} Vehicle name: {new_bus.name} Speed: {new_bus.max_speed} Mileage: {new_bus.mileage}')
print(f'Color: {new_car.color} Vehicle name: {new_car.name} Speed: {new_car.max_speed} Mileage: {new_car.mileage}')
print(new_bus.seating_capacity())
print(f'Total bus fare is ${int(new_bus.fare())}')
print(type(new_bus))
print(isinstance(new_bus, Vehicle))

