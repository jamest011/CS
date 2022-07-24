'''
File: badge_generator.py
Author: James Thomas

Purpose: Display badge to screen for user.
'''
# Genereate id
import random
import string
from random import randint, randrange


# Get inputs
print()
print('Please enter the following information: ')
fname = input('First name: ')
lname = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
badgeNum = input('ID Number (if you do not have an ID # leave blank): ')
hair = input('Hair color: ')
eyes = input('Eye color: ')
month = input('Birth month: ')
exp = input('Have you finished training?: ')
print()

# output
print('Here is your ID Card:')
print('----------------------------------------')
print(lname.upper() + ', ' + fname.capitalize())
print(job.title())
if badgeNum:
    print(badgeNum)
else:
    print('ID: ' + str(random.randint(10, 99)) +
          '-' + str(random.randrange(1000, 9999)))
print()
print(email.lower())
print(phone)
print()
print("%-21s %s" % ('Hair: ' + hair.capitalize(), 'Eyes: ' + eyes.capitalize()))
print("%-21s %s" % ('Month: ' + month.capitalize(), 'Training: ' + exp.capitalize()))
print('----------------------------------------')
