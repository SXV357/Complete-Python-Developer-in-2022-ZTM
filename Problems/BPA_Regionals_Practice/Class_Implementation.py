# 1
class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity=50, color="Blue"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.capacity = capacity

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

    def fare(self):
        return self.capacity * 100

    def print_info(self, color="White"):
        return f"Color: {color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


car = Vehicle("Honda", 240, 36, 50)
print(f'{car.max_speed}, {car.mileage}, {car.color}')

# 2
class Vehicle2:
    pass


new_vehicle = Vehicle2()
print(type(new_vehicle))

# 3
class Bus(Vehicle):
    def seating_capacity(self):
        return super().seating_capacity()

    def print_info(self):
        return super().print_info()

    def fare(self):
        initial_sum = super().fare()
        return f'Total bus fare is: {1.1 * initial_sum}'


bus = Bus("Volvo", 165, 26)
print(f'{bus.max_speed}, {bus.mileage}')
print(bus.seating_capacity())
print(bus.print_info())
print(bus.fare())
print(isinstance(bus, Vehicle))
print(isinstance(bus, Vehicle2))
print(isinstance(bus, Bus))

# 4
class Car(Vehicle):
    def print_info(self, color="White"):
        return super().print_info(color)


car2 = Car("Audi Q5", 240, 18)
print(car2.print_info())

# 5
class IntegerToRoman:
    def __init__(self, num):
        self.num = num

    def convert(self):
        mappings = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        nums = [k for k in mappings.keys()]
        roman = "" 
        i = 0
        while self.num > 0:
            for _ in range(self.num // nums[i]):
                roman += mappings[nums[i]]
                self.num -= nums[i]
            i += 1
        return roman

number = IntegerToRoman(4000)
print(number.convert())

# 6
class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman

    def convert(self):
        mappings = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        result = 0
        for i in range(len(self.roman)):
            if mappings[self.roman[i]] > mappings[self.roman[i - 1]]:
                result += mappings[self.roman[i]] - mappings[self.roman[i - 1]]
            else:
                result += mappings[self.roman[i]]
        return result

roman = RomanToInteger("MMMM")
print(roman.convert())