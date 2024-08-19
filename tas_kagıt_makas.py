import random

def rock_paper_scissor_HASIBENUR_TUNC():
    print("""
    Hello, welcome to the rock paper scissors game. The rules of our game are as follows:
    1-Rock beats scissors by breaking them.
    2-Paper beats the rock by wrapping it.
    3-Scissors beat the paper by cutting it.
    4-If two players choose the same move, the game ends in a draw.
    Our game is played as follows:
    -Each round can end with you winning, the computer winning or a draw.
    -The winner of the first two rounds wins the game.
    -You can press press the ‘q’ key to exit the game.
    Let's start!
    """)
    list = ['rock','paper','scissor']

    numberOfGamesPlayed = 0
    playerWins = 0
    computerWins = 0

    while True:
        numberOfGamesPlayed += 1
        playerWins = 0
        computerWins = 0

        while playerWins < 2 and computerWins < 2:
            print('Please select one of three options(rock, paper or scissor) /// press ‘q’ to exit ')
            playerChoice = input('Your choice is :').lower()

            if playerChoice == 'q':
                print('Quitting the game')
                return  
            if playerChoice not in list:
                print('This is an invalid login. Please enter a valid login')
                continue

            computerChoice = random.choice(list) 
            print(f"Computer choice : {computerChoice}")

            if playerChoice == computerChoice:
                print('A state of equality is a draw')
            elif (playerChoice == 'paper' and computerChoice == 'rock' ) or \
                 (playerChoice == 'rock' and computerChoice == 'scissor') or \
                 (playerChoice == 'scissor' and computerChoice == 'paper'):
                print('Player wins this round!')
                playerWins += 1
            else:
                print('Computer wins this round!')
                computerWins += 1

            print(f"Number of game played = {numberOfGamesPlayed}  "
                  f"Player wins = {playerWins}  "
                  f"Computer wins = {computerWins}  ")

        if playerWins == 2:
            print('The player wins the game.')
        else:
            print('The computer wins the game')

        options = ['yes', 'no']
        player_continue = input('Do you want to continue the game? (Yes/No):').lower()
        computer_continue = random.choice(options)
        print(f"Computer continue is : {computer_continue}")

        if player_continue == 'yes' and computer_continue == 'yes':
            print('The game continues')
        else:
            print('The game is over')
            break

rock_paper_scissor_HASIBENUR_TUNC()




