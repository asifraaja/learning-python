import random

MAX_GUESS = 5
minimumGuesses = 7
guesses = 0

print('Hello!!! What\'s your name')
name = input()

min = 0
max = 200
print('Hello ' + name + ". I am thinking a number between " + str(min) + " and " + str(max))

while True :
    randomNumber = random.randint(min, max)
    print('High Score : ' + str(minimumGuesses))
    while True :
        if(guesses >= MAX_GUESS):
            guesses = 0
            print('My Secret number was : ' + str(randomNumber) + ' Better luck next time :(')
            break
        print('Enter your Guess', end=' : ')
        data = input()
        guess = int(data)
        if guess > randomNumber :
            print('Your guess is too high')
            guesses += 1
        elif guess < randomNumber :
            print('Your guess is too low')
            guesses += 1
        else :
            guesses += 1
            print('Hurray !!! Your guessed it right. You guessed in ' + str(guesses) + ' moves')
            if(minimumGuesses > guesses) :
                minimumGuesses = guesses
            guesses = 0
            break
    print('Would you like to play again : Y/N')
    playAgain = input()
    if(playAgain == 'N') or (playAgain == 'n') :
        break