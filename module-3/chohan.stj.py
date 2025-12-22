"""Cho-Han, by Al Sweigart al@inventwithpython.com
Modified for CSD-325 Module 3 Assignment

Changes:
- Input prompt changed to initials (stj:)
- House fee changed to 12%
- Bonus added for dice roll total of 2 or 7
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# Program introduction with bonus notice
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS RULE:
If the dice roll total is 2 or 7, the player receives a 10 mon bonus.
''')

purse = 5000

while True:  # Main game loop
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('stj: ')  # Initials prompt
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_total = dice1 + dice2

    # Bonus for rolling 2 or 7
    if dice_total == 2 or dice_total == 7:
        print(f'You rolled a total of {dice_total}! You receive a 10 mon bonus!')
        purse += 10

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the dice.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Player bet
    while True:
        bet = input('> ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    # Reveal dice
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine winner
    rollIsEven = dice_total % 2 == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Results
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        house_fee = pot * 12 // 100  # 12% house fee
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        print('You lost!')
        purse -= pot

    # Check purse
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()