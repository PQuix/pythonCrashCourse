import random

hands = ['rock', 'paper', 'scissors']

while True:
    throw = input('\nWhat do you select?\n1. Rock\n2. Paper\n3. Scissors\n\nPlease press a corresponding number.\n')
    if throw == '1':
        throw = 'rock'
    elif throw == '2':
        throw = 'paper'
    elif throw == '3':
        throw = 'scissors'
    else:
        break

    op_throw = random.choice(hands)

    print("\nYou throw " + throw + "!")
    print("Opponent throws " + op_throw + "!")
    
    if throw == op_throw:
        print("DRAW!")
    elif throw == 'rock':
        if op_throw == 'scissors':
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
    elif throw == 'paper':
        if op_throw == 'rock':
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
    elif throw == 'scissors':
        if op_throw == 'paper':
            print("YOU WIN!")
        else:
            print("YOU LOSE!")