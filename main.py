import random
Num_Digits = 3
Max_Guesses = 3
def main():
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' you have {} guesses to get it.'.format(Max_Guesses))

        numGuesses = 1
        while numGuesses <= Max_Guesses:
            guess = ''
            while len(guess) != Num_Digits or not guess.isdecimal():
                print('guess #{}: '.format(numGuesses))
                guess= input('> ')
            clues = getclues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > Max_Guesses:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        print('Do you want to play again? (Yes or No)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for Playing!')
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(Num_Digits):
        secretNum += str(numbers[i])
    return secretNum

def getclues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues= []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagles'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ =='__main__' :
    main()
