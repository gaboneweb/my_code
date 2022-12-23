import random


def main_game_loop():
    print('''
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.
    I have thought up a number.
      You have 10 guesses to get it.
    ''')
    secretNum = getSecretNum()
    print(secretNum)
    num_of_guesses = 10
    current_guess = 1
    while current_guess <= num_of_guesses:

        print(f"Guess #{current_guess}")
        guess = input("> ")
        clue = getClues(guess,secretNum)
        print(clue)
        if clue == "You got it.":
            break

        current_guess += 1 



def getSecretNum():
    nums = [0,1,2,3,4,5,6,7,8,9]
    secNum = ''
    while len(secNum) < 3:
        sel = random.choice(range(10))
        if str(sel) not in secNum:
            secNum += str(sel)
        else:
            continue

    return secNum

def getClues(guess,secretNum):
    if guess == secretNum:
        return 'You got it.'
    guess_list = []
    for i in range(3):
        if guess[i] == secretNum[i]:
            guess_list.append('Fermi')
        elif guess[i] in secretNum:
            guess_list.append('Pico')

    if len(guess_list) == 0:
        return 'Bagels'
    else:
        guess_list.sort()
        return " ".join(guess_list)



if __name__ == "__main__":
    main_game_loop()
