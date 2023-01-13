import math
import random

#1
def fix34(arr):
    # Case 1 = Only one 3 in the array
    if arr.count(3) == 1:
        first = arr[0: arr.index(3) + 1]
        remaining = arr[arr.index(3) + 1 : len(arr)]
        reversed = sorted(remaining, reverse = True)
        first.extend(reversed)
        return first
    # Case 2 = > one 3 in the array
    elif arr.count(3) > 1:
        for i in range(len(arr) - 2):
            if arr[i + 2] == 4 and arr[i] == 3 and arr[i + 1] != arr[i] and arr[i + 1] != arr[i + 2]:
                arr[i + 1], arr[i + 2] = arr[i + 2], arr[i + 1]
                break
            sliced = arr[0: arr.index(4) + 1]
            remaining = arr[arr.index(4) + 1: len(arr)]
            for j in range(len(remaining) - 1):
                if remaining[j] == 3 and remaining[j - 1] == 4 and remaining[j + 1] != remaining[j] and remaining[j + 1] != remaining[j - 1]:
                    remaining[j - 1], remaining[j + 1] = remaining[j + 1], remaining[j - 1]
                    break
            sliced.extend(remaining)
            return sliced

#2
def score_statistics(file):
    new_file = open(file, mode = 'r')
    scores = []
    for score in new_file:
        scores.append(int(score.strip()))
    average = sum(scores) / len(scores)
    variance_sum = 0
    for i in range(len(scores)):
        variance_sum += pow(scores[i] - average, 2)
    print(f'Number of elements: {len(scores)}\n')
    print(f'Average: {average}')
    print(f'Min Value: {min(scores)}')
    print(f'Max Value: {max(scores)}')
    print(f'Standard Deviation: {round(math.sqrt(variance_sum / len(scores) - 1), 3)}')
    first, second, third, fourth = list(range(0, 25)), list(range(25,50)), list(range(50,75)), list(range(75, 101))
    first_count, second_count, third_count, fourth_count = 0,0,0,0
    for val in scores:
        if val in first:
            first_count += 1
        elif val in second:
            second_count += 1
        elif val in third:
            third_count += 1
        elif val in fourth:
            fourth_count += 1
    print(f'Quartile 1: {first_count}')
    print(f'Quartile 2: {second_count}')
    print(f'Quartile 3: {third_count}')
    print(f'Quartile 4: {fourth_count}')

#3
def order():
    subtotal = 0
    while True:
        print("Menu:")
        print("1) Regular Coffee ($7.99)")
        print("2) Breakfast Croissant ($5.99)")
        print("9) Total the order")
        print("0) Exit")
        print(f'Subtotal: ${subtotal}')
        selection = int(input("Your selection: "))
        while selection in [1,2,9,0]:
            try:
                if selection == 1:
                    print("Regular Coffee:")
                    try:
                        cream = str(input("Do you want cream for $0.10 more? (y/n): ")).lower()
                        if cream == "y" or cream == "yes, please!" or cream == "yes":
                            subtotal += 0.10 + 7.99
                            sugar = str(input("Do you want sugar for $0.15 more? (y/n): ")).lower()
                            if sugar == "y" or sugar == "yes, please":
                                subtotal += 0.15
                                print(f'Adding Regular coffee for ${subtotal}')
                            elif sugar == "n" or sugar == "no":
                                print(f'Adding Regular Coffee for ${subtotal}')
                        elif cream == "n" or cream == "no":
                            sugar = str(input("Do you want sugar for $0.15 more? (y/n): ")).lower()
                            if sugar == "y" or sugar == "yes, please":
                                subtotal += 0.15 + 7.99
                                print(f'Adding Regular coffee for ${subtotal}')
                            elif sugar == "n" or sugar == "no":
                                print(f'Adding Regular Coffee for ${7.99}')
                    except ValueError:
                        print("Error: Invalid Input")
                elif selection == 2:
                    print("Breakfast Croissant:")
                    try:
                        ham = str(input(("Do you want ham for $0.50 more? (y/n): "))).lower()
                        if ham == "y" or ham == "yes, please" or ham == "yes":
                            subtotal += 0.50 + 5.99
                            cheese = str(input("Do you want cheese for $0.25 more? (y/n): ")).lower()
                            if cheese == "y" or cheese == "yes, please" or cheese == "yes":
                                subtotal += 0.25
                                print(f'Adding Breakfast Croissant for ${subtotal}')
                            elif cheese == "n" or cheese == "no":
                                print(f'Adding Breakfast Croissant for ${subtotal}')
                        elif ham == "no" or ham == "n":
                            cheese = str(input("Do you want cheese for $0.25 more? (y/n): ")).lower()
                            if cheese == "y" or cheese == "yes, please" or cheese == "yes":
                                subtotal += 0.25 + 5.99
                                print(f'Adding Breakfast Croissant for ${subtotal}')
                            elif cheese == "n" or cheese == "no":
                                print(f'Adding Breakfast Croissant for ${5.99}')
                    except ValueError:
                        print("Error: Invalid Input")
                elif selection == 9:
                    print(f'Subtotal: {subtotal}')
                    print(f'Tax (10%): $2.08')
                    print(f'Total: ${subtotal + 2.08}')
                    print(f'Please have the customer pay ${subtotal + 2.08}. Thank you!')
                    subtotal = 0
                elif selection == 0:
                    print("Goodbye!")
                    break
            except ValueError:
                print("Error: Invalid Input")

def pointOfSale():
    randNum = random.randint(10, 20)
    while True:
        password = input(f'Enter password ({randNum}): ')
        digits = []
        for i in range(len(password)):
            if password[i].isdigit():
                digits.append(password[i])
        if not sum([int(i) for i in digits]) == randNum:
            print("Incorrect Password")
        else:
            order()

#4
def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

def is_perfect(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) == n

def display_prime_and_perfect():
    num = int(input("Enter a number: "))
    print(f'Prime numbers that exist between 0 and {num}: ')
    for i in range(num):
        if is_prime(i):
            print(i, end = ", ")
    print("\n")
    print(f'Perfect numbers that exist between 0 and {num}: ')
    for j in range(num):
        if is_perfect(j):
            print(j, end = ", ")
    print("\n")
    run_again = str(input("Would you like to run the program again? (y/n): ")).lower()
    if run_again == "y" or run_again == "yes":
        while True:
            num = int(input("Enter a number: "))
            print(f'Prime numbers that exist between 0 and {num}: ')
            for i in range(num):
                if is_prime(i):
                    print(i, end = ", ")
            print("\n")
            print(f'Perfect numbers that exist between 0 and {num}: ')
            for j in range(num):
                if is_perfect(j):
                    print(j, end = ", ")
            run_again = str(input("Would you like to run the program again? (y/n): ")).lower()
            if run_again == "n" or run_again == "no":
                break

display_prime_and_perfect()
