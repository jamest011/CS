'''
File: life_expectancy.py
Author: James Thomas

Purpose: Grab information from a file to get life expectancy information. 
'''

print()
user_year = int(input('Enter the year of interest: '))
avg = 0
num_user_years = 0

# get the overall max and min life expectancy from the file
with open("life-expectancy.csv") as life_file:
    next(life_file)
    lowest_country = ''
    lowest_year = -1
    lowest_age = 9999999
    highest_year = 9999999999
    highest_age = -1
    highest_country = ''
    min_country = ''
    min_age = 999999999
    max_age = -1
    max_country = ''

    for line in life_file:
        clean_line = line.strip()
        parts = clean_line.split(",")

        countries = parts[0]
        abv = parts[1]
        years = int(parts[2])
        life_exp = float(parts[3])

        if life_exp < lowest_age:
            lowest_age = life_exp
            lowest_country = countries
            lowest_year = years
        if life_exp > highest_age:
            highest_age = life_exp
            highest_country = countries
            highest_year = years
        if years == user_year:
            avg = avg + life_exp
            num_user_years = num_user_years + 1

            if life_exp > max_age:
                max_age = life_exp
                max_country = countries
            if life_exp < min_age:
                min_age = life_exp
                min_country = countries

avg = avg / num_user_years
print()
print(
    f'The overall max life expectancy is: {highest_age:.2f} from {highest_country} in {highest_year} ')
print(
    f'The overall min life expectancy is: {lowest_age:.2f} from {lowest_country} in {lowest_year}')
print()

# get the year from the user and display average life expectancy, min and max life expectancy and the country associated with the year entered

print(f'For the year {user_year}:')
print(
    f'The average life expectancy across all countries in {user_year} was {avg:.2f}')
print(f'The max life expectancy was in {max_country} with {max_age:.2f}')
print(f'The min life expectancy was in {min_country} with {min_age:.2f}')
print()
