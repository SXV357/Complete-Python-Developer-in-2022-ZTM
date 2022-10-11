# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
basket.pop(0)
# 2. Remove "Blueberries" from the list.
basket.pop(2)
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
# 5. Count how many apples in the basket
basket.count("Apples")
# 6. empty the basket
basket.clear()
print(basket)


#fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
friends.extend(["Stanley"])
friends.sort()
print(friends)



#list unpacking(similar to JS spread operator)
alpha, beta, gamma, *delta, epsilon = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(epsilon) # points to last value in the list
print(delta)
