import random

list_of_words = ['apple','loose','orange','assets', 'businessman']

randomword = list(random.choice(list_of_words))

hiddenword = list(len(randomword) * '_')

attempts = len(randomword)

def check_attempts():
    global attempts
    attempts -= 1
    print(f'you have {attempts} attempts left')
    if attempts == 0 and '_' in hiddenword:
        print('game over'.upper())
        exit()


while '_' in hiddenword:

    letter1 = input('give me a letter ')

    if letter1 in hiddenword:
        if letter1 in randomword:
            print('you already have guessed that')
            check_attempts()

    if letter1 in randomword:

        for i, value in enumerate(randomword):
            if value == letter1:
                hiddenword[i] = value
        print(''.join(hiddenword))
    elif letter1 not in randomword:
        print('not in a word')
        check_attempts()

else:
    print('you won')
