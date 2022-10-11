import random


def check_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct!")
            return True
    else:
        print("Only numbers from 1-10 allowed")
        return False


if __name__ == '__main__':
    random_num = random.randint(1, 10)
    while True:
        try:
            user_input = int(input("Guess a number from 1-10: "))
            if check_guess(user_input, random_num):
                break
        except ValueError:
            print("No strings allowed")
            continue
