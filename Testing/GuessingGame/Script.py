from random import randint


def check_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            return True
    return False

# print(check_guess(10, 20))


answer = randint(1, 10)


def run_game():
    while True:
        try:
            user_guess = int(input("Guess a number between 1-10: "))
            if check_guess(user_guess, answer):
                print("You got it right!")
                break
        except ValueError:
            print("Only integers allowed")


if __name__ == '__main__':
    run_game()
