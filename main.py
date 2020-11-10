import random
import time


def choice():
    '''
    Function choice returns the number entered by the user.
    If user entered not a number, the function will ask to enter data until the data is of type int.
    '''
    while True:
        try:
            number = int(input('Enter a number between 1 and 49: '))
            break
        except ValueError:
            print('It is not a number!')
    return number


def user_numbers():
    '''
    Function user_numbers checks if if the user has entered a number from 1 to 49
    and if the number has not been repeated before.
    :your_numbers type: list
    :return: a list of 6 numbers
    '''
    your_numbers = []
    while len(your_numbers) < 6:
        number = choice()
        if number not in your_numbers and 0 < number < 50:
            your_numbers.append(number)
    return your_numbers


def computer_numbers():
    '''
    Function computer_numbers makes a list of 6 random numbers from 1 to 49.
    :pc_numbers type: list
    :value type: int
    :return: a list of numbers
    '''
    pc_numbers = []
    for _ in range(6):
        value = random.randint(1, 49)
        pc_numbers.append(value)
    print(f'The numbers are drawn: {pc_numbers}.')
    time.sleep(2)
    return pc_numbers


def lotto():
    '''
    Function lotto compares the selected numbers by the user and the computer.
    If the matching numbers are 3,4,5 or 6 - the user won. Otherwise, he lost.
    :sort_list type: list
    :result type: list
    '''
    list_users_numbers = user_numbers()
    sort_list = sorted(list_users_numbers)
    print(f'Your numbers are: {sort_list}.')
    time.sleep(2)

    comp_numbers = computer_numbers()

    result = list(set(sort_list) & set(comp_numbers))

    if len(result) < 2:
        print(f'Number of numbers hit: {len(result)} \nUnfortunately you lose. Try to play again.')
    else:
        print(f'Number of numbers hit: {len(result)} \nCongratulations! You win! Numbers won: {result}')


if __name__ == '__main__':
    lotto()
