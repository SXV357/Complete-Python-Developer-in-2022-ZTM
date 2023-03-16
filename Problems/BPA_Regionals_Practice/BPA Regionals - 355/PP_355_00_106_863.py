# Contestant Number: 00106863

from random import randrange

def get_number_in_dials():
    """
    How many random numbers in each lock
    """
    dials = int(input("Each lock has how many dials? "))
    return dials

def get_how_many_to_list():
    """
    How many combinations to be generated
    """
    combinations = int(input("How many combinations should I generate? "))
    return combinations

def get_number(minimum, maximum):
    """
    Returns random number between 0 and 9 inclusive
    """
    return randrange(minimum, maximum)

def next_combo_number():
    # The program will ask the question "Each lock has how many dials" 2x because of assigning
    # "value" to get_number_in_dials initially, but it will eventually get to the next question
    # and then display the output as specified in the instructions.
    """
    Utilizes number of random numbers per combination and number of combinations to 
    print out all the possible combinations to the user, including how many were generated
    """
    counter = 0
    value = get_number_in_dials()
    if get_number_in_dials() >= 3:
        for i in range(1, get_how_many_to_list() + 1):
            counter += 1
            string_rep = ""
            for j in range(value):
                individual_num = get_number(0, 9)
                string_rep += str(individual_num) + " "
            print(f'Number {i}: {string_rep}')
        print("\n")
        print(f'{counter} combinations were generated')
    else:
        print('Error: Number of dials needs to be >= 3')
      
next_combo_number()