# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

print('What is your name?')
userName = input()
print('What age are you?')
age = int(input())
centYear = 100-age
turn100 = 2019+centYear
print(userName + ' will turn 100 in the year ' + str(turn100))

print('Enter a number')
number = int(input())
loops = 0

while loops < number:
    print(userName + ' will turn 100 in the year ' + str(turn100))
    loops = loops + 1
