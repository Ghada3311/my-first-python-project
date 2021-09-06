# my-first-python-project
# this file is requirment to pass python101 on SATR platform,
# all code is created by Ghadah Aladwani

telephone_book = {
    '1111111111': 'Amal',
    '2222222222': 'Mohammed',
    '3333333333': 'Khadijah',
    '4444444444': 'Abdullah',
    '5555555555': 'Rawan',
    '6666666666': 'Faisal',
    '7777777777': 'Layla'}


def check_number(number):
    if len(number) == 10:
        return True
    elif len(number) != 10:
        return False


def main_page():
    print('Enter N to Search by numbers')
    print('Enter F to search by names')
    print('Enter E to exit')
    x = input()
    return x


def return_name(val):
    for key, value in telephone_book.items():
        if val == value:
            return key

    return 'Not found!'


def return_number(k):
    if k in telephone_book:
        return telephone_book[k]
    elif k not in telephone_book:
        return 'Sorry, This Number Is Not Found!'


i = main_page()

while i != 'E':
    if i == 'N':
        phone_number = input('Enter Number: ')
        if check_number(phone_number):
            print(return_number(phone_number))
            i = main_page()
        elif not check_number(i):
            print('Invalid Input! Please enter only 10 digit numbers! ')
            i = main_page()
    elif i == 'F':
        name = input('Enter Name: ')
        print(return_name(name))
        i = main_page()

print('end')

