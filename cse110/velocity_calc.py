import math

print('Welcome to the velocity calculator. Please enter the following:')
print()

# prompt user input

m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 100 for water): '))

# comment out 'A' when looking for the terminal velocity of the bowling ball
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# bowling ball info
bowling_ball = math.pi*4.25**2

# equations
c = (1 / 2) * p * bowling_ball * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
vt = math.sqrt(m * g / c)

print()

# display results
print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after {t} seconds is: {v:.3f} m/s')
print(f'The terminal velocity is: {vt} ')
