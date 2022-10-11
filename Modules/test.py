import random
# import sys

# start = sys.argv[1]
# end = sys.argv[2]
randomNumber = random.randint(1, 100)
while True:
    try:
        user_input = int(input('Guess a number between 1 and 100: '))
        if user_input == randomNumber:
            print('You got it right!')
            break
        elif user_input < randomNumber:
            print('Your guess was lesser than actual number')
        elif user_input > randomNumber:
            print('Your guess was higher than actual number')
    except ValueError:
        print('Only numbers allowed')
        continue

# print(random)
# print(help(random))
# print(dir(random))

# random.random() # generates random number between 0-1
# random.randint(start, end) # generates random number between start and end
# random.choice(iterable) # picks a random value from the iterable
# random.shuffle(iterable) # shuffles the iterable in place and returns none if printed directly

# i can create a separate file on my desktop, import sys there and use the .argv method to 
# access argument at 2nd and 3rd index that has been passed via the terminal after the file run command

#example: python filename.py argument 1 argument 2(.argv[1] and .argv[2]) represent 1st and 2nd argument respectively