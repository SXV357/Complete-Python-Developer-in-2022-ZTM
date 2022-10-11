# tuples

# tuples are immutable
new_tuple = (1, 2, 3, 4, 5, 1, 3, 1)
# new_tuple[0] = 10 # this will throw an error
print(new_tuple[3]) # like a list and individual valuews can be accessed
print(100 in new_tuple)
print(new_tuple.index(5))
print(new_tuple.count(1))
# #list slicing and list unpacking can be used with tuples
print(new_tuple[::-1])
print(new_tuple[::2])
x, y, z, *iphone = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(iphone) # will return a list
print(len(iphone) == 10)
print(len(new_tuple) > len(iphone))

# #sets

# #sets are unordered collections of unique elements
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}
print(set_1) # the 2nd 10 won't appear because only unique elements are printed

my_list = [1,2,3,4,5,5]
new_list = list(set(my_list)) # removes duplicates and returns and array w unique values
print(new_list)
# print(my_list[0]) # throws an error because indexing isn't supported for sets

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.difference(s2))
# # s1.difference_update(s2) # removes the values in s2 from s1(4 and 5)
# # print(s1)
print(s1.intersection(s2)) # returns the common values in both sets
print(s1.isdisjoint(s2)) # returns false since both sets have common values
print(s1.union(s2)) # returns all the values in both sets
print(s1.issubset(s2)) # returns true if the entirety of s1 is a subset of s2





# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school 
# principal can use to immediately 
# find out who missed class so they can call the parents. 
# (Imagine if the list had 1000s of students. 
# The principal can use the lists generated by the teachers + 
# the school database to use python and make his/her job easier): Find the students that miss class!

updated_attendance_list = set(attendance_list)
print(school.difference(updated_attendance_list))