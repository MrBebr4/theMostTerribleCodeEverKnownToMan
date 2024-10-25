import random   # Importing random module

moves = ['rock', 'paper', 'scissors'] # List of possible moves
playerChoise = input('rock, paper or scissors? ')
computerChoise = random.choice(moves)

#all possible outcomes
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
        print('Computer wins!') #we don't need to check all possible outcomes, because if player wins, computer loses

else:
    print('Invalid input') #if player inputs something else than rock, paper or scissors, print invalid input
    exit()