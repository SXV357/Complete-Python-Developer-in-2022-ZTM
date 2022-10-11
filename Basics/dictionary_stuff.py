# keys need to be immutable
# keys can be overwritten

new_dict = {
    "k1": 10,
    "k2": [45, 46, 47]
}
print(new_dict["k1"]) # k1 no longer equqals 10, it now equals [45, 46, 47]

#can specify a default value for .get() method in case the key doesn't exist

# key can also equal a tuple

some_dict = {
    (1, 2, 3): "value1",
}
print(some_dict[(1,2,3)])

# #alternate way to create dictionary

dict_2 = dict(k1=10, k2=20, k3=30)
print(dict_2)
print(dict_2.items())
print(10 in dict_2.keys())
dict_2.popitem()
print(dict_2)
dict_3 = dict_2.copy()
print(dict_3)




#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
main_user = {
    "age": 17,
    "username": "Shre_Vis",
    "weapons": ["AK47", "M82", "PKM"],
    "is_active": True,
    "clan": "United States of America"
}
#2 iterate and print all the keys in the above user.
print(main_user.keys())
#3 Add a new weapon to your user
main_user.update({"weapons": ["AK47", "M82", "PKM", "M4A1"]})
#4 Add a new key to include 'is_banned'. Set it to false
main_user.update({"is_banned": False})
#5 Ban the user by setting the previous key to True
main_user.update({"is_banned": True})
#6 create a new user2 my copying the previous user and update the age value and username value. 
user2 = main_user.copy()
user2.update({"age": 13, "username": "Harsh_Vis"})
print(user2)