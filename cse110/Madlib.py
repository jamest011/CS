'''
File: Madlib.py
Author: James Thomas

Purpose: Display madlib game with user inputs.
'''

# Word lists for the generated option
import random
adjectives = ['angry', 'bad', 'big', 'bitter', 'black', 'bland', 'bloody', 'blue', 'bold', 'chewy', 'chubby', 'classy', 'clever', 'close', 'cloudy', 'clumsy', 'busy', 'deadly', 'deep', 'dense', 'easy', 'faint', 'fair', 'fancy',
              'hairy', 'handy', 'happy', 'hip', 'icy', 'little', 'nice', 'noisy', 'odd', 'oily', 'quiet', 'rare', 'sincere', 'small', 'smart', 'smelly', 'sore', 'sweaty', 'sweet', 'tall', 'tiny', 'tough', 'true', 'ugly', 'warm', 'weak']
animals = ['aardvark', 'alpaca', 'baboon', 'beaver', 'tiger', 'elephant', 'toad', 'cat', 'centipede', 'chameleon', 'cheetah', 'chipmunk', 'dragonfly', 'duck', 'dog', 'ferret', 'fox', 'frog', 'penguin', 'fenek fox', 'shark', 'gecko', 'giraffe', 'gorilla', 'goose', 'duck', 'iguana', 'komodo dragon', 'goat', 'honeybadger', 'bee', 'rabbit', 'red panda', 'panda', 'rattlesnake', 'rhino', 'seaslug', 'sea urchin', 'sheep', 'sloth', 'snail', 'skunk', 'raccoon', 'snake', 'stingray', 'grizzly bear', 'tortoise', 'tuna', 'bass', 'polar bear', 'tasmanian devil', 'hummingbird', 'vampire bat', 'fruit bat', 'vulture', 'albatross', 'warthog', 'walrus', 'whale shark', 'wolf', 'water buffalo', 'bison', 'wombat', 'yak', 'zebra', 'lion', 'horse', 'leopard', 'donkey', 'antelope', 'caribou',
           'armadillo', 'black bear', 'penguin', 'arctic wolf', 'ant', 'axolotl', 'python', 'boobie', 'black widow spider', 'tarantula', 'chikadee', 'eagle', 'chicken', 'rooster', 'hawk', 'seagull', 'crow', 'cuttlefish', 'coyote', 'manta ray', 'crocodile', 'alligator', 'caiman', 'elephant seal', 'manatee', 'orca', 'narwhal', 'beluga', 'lemur', 'gerbil', 'hamster', 'chinchilla', 'guppy', 'raven', 'tropical crow', 'hedgehog', 'procupine', 'humpback whale', 'hippo', 'cow', 'bull', 'pig', 'kangaroo', 'monkey', 'kiwi', 'dodo bird', 'ladybug', 'llama', 'penguin', 'hare', 'moose', 'reindeer', 'parrot', 'rat', 'mouse', 'pelican', 'peacock', 'pomeranian', 'piranha', 'puffin', 'black bear', 'ocelot', 'serval', 'puma', 'mountain lion', 'possum', 'snow leopard', 'jellyfish', 'octopus']
verbs = ['act', 'arrange', 'break dance', 'build', 'coach', 'color', 'cough', 'cry', 'dance', 'draw', 'drink', 'eat' 'edit', 'exit', 'imitate me', 'invent waffles', 'jump', 'laugh',
         'lie', 'listen to rap', 'paint', 'plan', 'play', 'read', 'run', 'scream', 'shout', 'sing', 'skip', 'sleep', 'sneeze', 'study', 'teach', 'clean', 'twirl', 'pout', 'win', 'write', 'whistle']
exclamations = ['Ah', 'Aha', 'Ahem', 'Alas', 'Amen', 'Aw', 'Awesome', 'Aww', 'Bada-bing', 'Bah', 'Baloney', 'Big deal', 'Bingo', 'Boo', 'Boo-hoo', 'Booyah', 'Boy oh boy', 'Bravo', 'Brilliant', 'Brrr', 'Bull', 'Bye', 'Cheers', "C'mon", 'Cool', 'Cowabunga', 'Dang',
                'Darn', 'Dear me', 'Duck', 'Duh', 'Eh', 'Enjoy', 'Excellent', 'Fabulous', 'Fantastic', 'Fiddledeedee', 'Finally', "For heaven's sake(s)", 'Fore', 'Foul', 'Freeze', 'Gee willikers', 'Giddyup', 'Good golly', 'Goodbye', 'Good grief', 'Good heavens', 'Gosh', 'Great']

mode = input(
    'Welcome to MadLib! Would you like to play or get one generated for you? (Play/Get): ')

if mode.lower() == 'play':
    print('Please enter the following:')
    adj = input('adjective: ')
    animal = input('animal: ')
    verb = input('verb: ')
    exc = input('exclamation: ')
    verb1 = input('verb: ')
    verb2 = input('verb: ')

    print()
    print('Your story is: ')
    print()
    print('The other day, I was really in trouble. It all started when I saw a very ')
    print(adj.lower() + ' ' + animal.lower() + ' ' + verb.lower() +
          ' down the hallway. "' + exc.capitalize() + '!" I yelled. But all ')
    print('I could think to do was to ' +
          verb1.lower() + ' over and over. Miraculously, ')
    print('that caused it to stop, but not before it tried to ' +
          verb2.lower() + ' right in front of my family.')
elif mode.lower() == 'get':
    print('Here is the Madlib generated for you:')
    adjR = random.choice(adjectives)
    animalR = random.choice(animals)
    verbR = random.choice(verbs)
    excR = random.choice(exclamations)
    verb1R = random.choice(verbs)
    verb2R = random.choice(verbs)

    print()
    print('Your story is: ')
    print()
    print('The other day, I was really in trouble. It all started when I saw a very ')
    print(adjR + ' ' + animalR + ' ' + verbR +
          ' down the hallway. "' + excR.capitalize() + '!" I yelled. But all ')
    print('I could think to do was to ' +
          verb1R + ' over and over. Miraculously, ')
    print('that caused it to stop, but not before it tried to ' +
          verb2R + ' right in front of my family.')
elif mode.lower() == 'Quit':
    print('Thank you for playing!')
else:
    mode = input(
        'Please enter Play, Get or Quit to end(Play/Get/Quit): ')
