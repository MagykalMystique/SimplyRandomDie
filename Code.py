import random as rd

rolling = True

answer = input('Would you like to roll the die? Please type True or False. ').lower()

while rolling == True:
    if answer == 'true':
        print('The die was rolled and the number is',rd.randint(1,6))
        answer = input('Would you like to roll the die? Please type True or False. ').lower()
    elif answer == 'false':
        rolling = False
    elif answer != 'true' or answer != 'false':
        print('I do not comprehend this unitelligent gibberish, peasant.')
        # maybe this print is a little too sassy lololol
        answer = input('Would you like to roll the die? Please type True or False. ').lower()
