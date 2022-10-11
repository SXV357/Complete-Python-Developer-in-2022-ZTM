# built in modules can let us access specialized data types
from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

print(Counter([1,2,3,4,5,4,6,7,7,9,9])) # returns dict with number of items each item in iterable occurs(hashmap)


d = defaultdict(int, {'a': 1, 'b': 2})
print(d['c']) # can provide a callable object for a key that doesn't exist and not run into any errors(returns 10)

d1 = OrderedDict()
d1['a'] = 45
d1['b'] = 55

d2 = OrderedDict()
d1['b'] = 45
d1['a'] = 45

print(d1 == d2) # keeps track of exact order in which keys and values were specified(returns false because order of insertion isn't the same)


print(datetime.time()) # by default returns 00:00:00
print(datetime.time(10, 30, 45)) # returns 10:30:45
print(datetime.date.today()) # returns current date
print(datetime.tzinfo()) # returns timezone info

new_arr = array('i', [i for i in range(101) if i % 6 == 0])
print(new_arr) # specify what data type the items in the array are of and then specify the array
new_arr.append(1000)
print(new_arr)
new_arr.reverse()
print(new_arr)