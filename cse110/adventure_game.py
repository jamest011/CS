'''
File: adventure_game.py
Author: James Thomas

Purpose: Display adventure game that gives user choices.
'''

#import random

print()
print('Welcome to the Adventure Game! A game of choices that let you decide your fate!')
print('                             Let us begin!')
print('-------------------------------------------------------------------------------')

print()

print("It's early Sunday morning and you decide to go for a walk on a trail you visit every week.\nWhen you arrive you notice a new, lightly used path in the grass on the left.")
print()
path = input(
    'Do you continue STRAIGHT down your normal path or do you venture LEFT down the new path? (Straight/Left or Q to Quit)\n')
print()


# Normal path
if path.lower() == 'straight':
    print('You walk down your normal route for about an hour before you realize that you are lost.')
    print()
    lost = input(
        'Should you continue STRAIGHT, stop and SCREAM for help or TURN AROUND?(straight/scream/turn around)\n')
    print()
    if lost.lower() == 'straight':
        print(
            "You look at your phone and notice another hour has past and you're still lost.")
        print('Frozen in fear, you scream for help, but there is no one around...')
        lost2 = input(
            'After screaming for a few minutes you hear a rustling in the woods next to you. Walk towards the rustling? (YES/NO)\n')
        print()
        if lost2.lower() == 'yes':
            print('As you approach the rustling, you see a women who asks you what is wrong. You tell her you are lost and she says to go north into the woods and you will find a nice surprise.')
            print(
                'You tell yourself that she must know a way out, right? She did just come from there.')
            listen = input('Do you listen to the woman?(YES/NO)\n')
            if listen.lower() == 'yes':
                print()
                print(
                    'You come across a carnival! As you approach the carnival disappears and you feel a touch on your shoulder. As you turn to see who it is...')
                print("A bright light is in your eyes. You try and cover them, but it's still too bright! you blink a few times and realize it's the police.")
                print('They ask if you are alright. You say yes. Then they ask why you are in the park naked. At this moment you realize that you forgot to take your medicine last night...')
                print("You know... the one your doctor gave you to help with your sleep walking. The police escort you home and you can't help but to feel embarrassed.\nThe end")
            else:
                print()
                print('You ignore her and wake up screaming from a nightmare. Confused your spouse jumps up and runs out of fear... What a rough start to the day.')
        else:
            print()
            print('You ignore the rustling, but it grows louder and louder and louder. Out of the woods comes a man with a teddy bear and a funnel cake.')
            print(
                'Puzzled, you ask him where he had come from. He tells you there is a carnival in the woods.')
            carnival = input(
                'Do you go to the CARNIVAL or do you continue to try and find your way HOME?(Carnival/Home)')
            print()
            if carnival.lower() == 'home':
                print(
                    'After a while of searching you find the end of the path. Scared, but relieved, you head home to get some rest.')
            else:
                print(
                    "Where did this come from? A carnival in the woods? What is this Coachella? I'm too old for this... or maybe... just maybe I should branch out a bit")
                print('After much thought and consideration you go to the carnival. Once you arrive you realize you left your wallet at home. The kind man from before offers to pay for you.')
                print('You think about it for a minute and agree. He gives you a tour of the carnival. After a few hours you decide to leave the carnival. Exhausted, you get some much needed rest.\nThe end.')

# scream choice
    elif lost.lower() == 'scream':
        print("You scream for help over and over again. No one seems to be near to hear you...")
        scream = input(
            'After screaming for a few minutes you hear a rustling in the woods next to you. Walk towards the rustling? (YES/NO)\n')
        if scream.lower() == 'yes':
            print()
            print('As you approach a puppy walks out of the bush. You turn around and head home with a new addition to your family!')
        elif scream.lower == 'no':
            print()
            print('Frozen in fear, the rustling gets louder and gets closer until a man with a giant teddy bear walks out.')
            print('He tells you about the carnival and tells you how to get there.')
            listen = input('Do you listen to this stranger?(YES/NO)\n')
            if listen.lower() == 'yes':
                print()
                print(
                    'You come across a carnival! As you approach you see your family and friends waiting to surprise you!\nThe end!')
            else:
                print()
                print('You ignore them and continue screaming down the same path over and over again. Forever lost in the woods... Never to be found.')
        else:
            print('Please double check your spelling and try again!')


# turn around choice
    elif lost.lower() == 'turn around':
        print('')
        print("As you turn around you see a moose. It's a bit small, but you are cautious. As it approaches you, the mother of that moose tramples you.")
        print('You wake up in the hospital... paralyzed... How could this have happened? You were just about to go for a walk and now this... Your career as a doctor is over...')
        print('OR IS IT?')
        print('Saddened by the situation, you set off to conquer your goals despite the drastic change in your life. Good luck on the next journey!\nYou got this!')

# New path
elif path.lower() == 'left':
    print('You hear what sounds like a crowd of people in the distance having fun. They are just off the new path a bit into the woods.')
    crowd = input('Continue towards the crowd? (YES/NO)\n')
    if crowd.lower() == 'yes':
        print('After venturing into the woods, you come across a large crowd.')
        closer = input(
            "You can't seem to see what's going on. Keep going closer?(YES/NO)\n ")
        if closer.lower() == 'yes':
            print()
            print("Someone is injured! Luckily, you're a doctor! You help the injured person and as a thanks, they pay you $15,000,000! You retire there after and travel the world with your family!")
        elif closer.lower() == 'no':
            print()
            print('As you walk by you see an ambulance pull up. They rush to the middle of the crowd and exit the crowd with a person on a gurney. You here them say that if someone would have been there a few minutes sooner the person would ahve lived.')
            print(
                "Could you have saved them? Could you have made a difference? You'll never know...")
        else:
            print('Please retry by entering the information without error.')
    elif crowd.lower() == 'no':
        print()
        print('As you turn from the carnival you jolt awake. This was all a dream? How could it have been? It felt so real!')
    else:
        print('Please double check your spelling and try again!')

# hidden path
elif path.lower() == 'go home':
    print("I see you don't like to explore. Well, go back, grab the family, relax and eat some ice cream. Ponder on the things you may have missed today. They could have been wonderful!\nThe end!")

# quit
elif path.lower() == 'q':
    print('Try using "GO HOME" for a new adventure.')
    print()
    print('Thank you for playing the Adventure Game. Have a great day!')
    print()

else:
    print('Please try again with one of the listed options or try "GO HOME" for a secret path.')
