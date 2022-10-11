#walrus operator(can be used to assign and return a value at the same time)

print((x := 15) > 10) # assigns 15 to n and returns boolean result
print(type((x := 15) > 10))

empty_list = []
while ((user_input := input("Enter a number: ")) != '0'): # assinging input to variable user_input
    empty_list.append(int(user_input))
    print(empty_list)

another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if (n := len(another_list)) > 5:
    print(f'The list is slightly long and  has {n} elements')

def compare_lengths(li1, li2):
    if (i := len(li1)) > (j := len(li2)):
        return f'List 1 which has {i} elements is longer than List 2 which has {j} elements'
    elif (i := len(li1)) < (j := len(li2)):
        return f'List 1 which has {i} elements is shorter than List 2 which has {j} elements'
    else:
        return f'List 1 which has {i} elements is the same length as List 2 which has {j} elements'
print(compare_lengths([1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10]))