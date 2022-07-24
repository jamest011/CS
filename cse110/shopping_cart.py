'''
File: shopping_cart.py
Author: James Thomas
Purpose: Create a shopping cart for users to add items to.
'''

# imports
import time

# variables
items = []
prices = []
number = -1

print()
print('Welcome to the Shopping Cart Program!')
print()


while number != 6:

    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Clear Cart')
    print('6. Quit')
    print()
    number = int(input('Please enter an action: '))
    print()

    if number == 1:
        item = input('What item would you like to add? ')
        price = float(input(f'What is the price of {item}? $'))

        items.append(item)
        prices.append(price)

        print(f"'{item}' has been added to the cart.")
        print()

    elif number == 2:
        if items:
            print('The contents of the shopping cart are:')

            for i in (n+1 for n in range(len(items))):
                print(f"{i}. {items[i-1]} - ${prices[i-1]:.2f}")

            print()

        else:
            print('Your cart is empty.\nReturning to menu.')
            print()

    elif number == 3:
        if items:
            print('Here is your list:')
            for i in (n+1 for n in range(len(items))):
                print(f"{i}. {items[i-1]} - ${prices[i-1]:.2f}")
            print()
            remove = int(input('Which item would you like removed? '))

            done = ''
            while done != 'no':
                if remove-1 not in range(len(items)):
                    print()
                    remove = int(input('Please enter a valid number: '))
                    print()
                    if remove-1 in range(len(items)):
                        del items[remove - 1]
                        print('Item removed')
                        print()

                done = input(
                    'Would you like to remove any more items? (Yes/No) ')
                print()

                if remove in range(len(items)):
                    del items[remove - 1]
                    print('Item removed.')
                    print()

        else:
            print('Your cart is empty.\nReturning to menu.')
            print()

    elif number == 4:
        if items:
            total = 0
            for i in (n+1 for n in range(len(items))):
                total += prices[i-1]
            print(f'Your total is: ${total:.2f}')
            print()
        else:
            print('Your cart is empty.\nReturning to menu.')
            print()

    elif number == 5:
        if items:
            check = input(
                'Are you sure you would like to clear your cart?(Y/N) ')
            if check.lower() == 'y':
                print()
                items.clear()
                print('Your cart has been cleared.\nReturning to the menu.')
                print()
            else:
                print('Returning to the menu.')

                print()
        else:
            print('Your cart is empty.\nReturning to menu.')
            print()


if number == 6:
    print('Thank you for shopping. Have a great day!')
    print()
