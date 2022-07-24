color = input('Please type your favorite color: ')

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
PURPLE  = '\033[35m'
WHITE   = '\033[37m'
CYAN    = '\033[36m'



if color.lower() == 'red':
    print(RED + 'Your favorite color is ' + color + '!')
elif color.lower() == 'blue':
    print(BLUE + 'Your favorite color is ' + color + '!')
elif color.lower() == 'green':
    print(GREEN + 'Your favorite color is ' + color + '!')
elif color.lower() == 'purple':
    print(PURPLE + 'Your favorite color is ' + color + '!')
elif color.lower() == 'white':
    print(WHITE + 'Your favorite color is ' + color + '!')
elif color.lower() == 'black':
    print(BLACK + 'Your favorite color is ' + color + '!')
elif color.lower() == 'yellow':
    print(YELLOW + 'Your favorite color is ' + color + '!')
elif color.lower() == 'teal' or 'cyan':
    print(CYAN + 'Your favorite color is ' + color + '!')
else:
    print('Your favorite color is ' + color +'!')