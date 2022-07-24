''' 
04 Prove: Assignment - Meal Price Calculator
Author: James Thomas
CSE 110
'''
print()
print()
print('Meal Price Calculator')
print()

# User input
child_meal = float(input("What is the price of a child's meal? $"))
adult_meal = float(input("What is the price of an adult's meal? $"))
num_kids = int(input('How many children are there? '))
num_adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the tax rate? '))

print()

subtotal = num_kids * child_meal + num_adults * adult_meal

# calculate user input
print(f'Subtotal: ${subtotal:.2f}')
tax = (tax_rate/100) * float(subtotal)
print(f'Sales Tax: ${tax:.2f}')
total = round(tax + float(subtotal), 2)
print(f'Total: ${total:.2f}')
print()


# option for splitting the check
split = input('Will you be splitting the check?(Y/N) ')
if split == 'Y'.lower():
    people = float(input('How many people will be paying? '))
    split_total = round((tax + float(subtotal)) / people, 2)
    print(f'The total per person is: ${split_total:.2f}')
    print()
    paid = input('What is the payment amount? $')
    change = float(paid) - split_total
    print(f'Change: ${change:.2f}')

else:
    paid = input('What is the payment amount? $')
    change = float(paid) - total
    print(f'Change: ${change:.2f}')
