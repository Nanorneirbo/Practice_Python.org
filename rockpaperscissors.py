# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import random as random
playAgain = "Y"
while playAgain == "y" or "Y":

    print('Player 1 pick please')
    p1Choice = str(input())

    while p1Choice != 'Rock' and p1Choice != 'Paper' and p1Choice != 'Scissors':
        print('Please try again you must enter Rock, Paper or Scissors')
        print(p1Choice)
        p1Choice = input()

    choices = ['Rock', 'Paper', 'Scissors']
    computerChoice = choices[random.randint(0, 2)]

    print(" player throws " + p1Choice)
    print(" Computer throws " + computerChoice)

    if computerChoice == p1Choice:
        print(' It s a Tie')
    elif p1Choice == 'Rock' and computerChoice == 'Paper':
        print('Computer Wins')
    elif p1Choice == 'Rock' and computerChoice == 'Scissors':
        print('P1 wins')
    elif p1Choice == 'Scissors' and computerChoice == 'Paper':
        print('P1 Wins')
    elif p1Choice == 'Scissors' and computerChoice == 'Rock':
        print('Computer wins')
    elif p1Choice == 'Paper' and computerChoice == 'Rock':
        print('P1 Wins')
    elif p1Choice == 'Paper' and computerChoice == 'Scissors':
        print('Computer wins')
    else:
        print('this means you done messed up the code!')

    print('Play Again Y or N')
    playAgain = input()

