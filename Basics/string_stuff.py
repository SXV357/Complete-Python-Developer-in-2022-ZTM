# new_string = "Bank of America"
# new_string += " is a great bank"
# print(new_string[::-1])

# age checker
birth_year = input("What year were you born?: ")
present_age = 2022 - int(birth_year)
print(f'You are {present_age} years old.')


# password checker
user_name = input("Enter your username: ")
password = input("Enter your password: ")

hidden_password = "*" * len(password)

print(f'{user_name}, your password {hidden_password} is {len(password)} characters long.')
