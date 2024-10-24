import random
moves = ['rock', 'paper', 'scissors']
playerChoise = input('rock, paper or scissors? ')
computerChoise = random.choice(moves)
if playerChoise in moves:
    print('Computer chose', computerChoise)
    if playerChoise == computerChoise:
        print('Tie!')
    elif playerChoise == 'rock' and computerChoise == 'scissors':
        print('Player wins!')
    elif playerChoise == 'paper' and computerChoise == 'rock':
        print('Player wins!')
    elif playerChoise == 'scissors' and computerChoise == 'paper':
        print('Player wins!')
    else:
        print('Computer wins!')

else:
    print('Invalid input')
    exit()