import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play_game(word):
    tries = 6
    words_guessed = []
    letters_guessed = []
    blanks = '-'*len(word)
    guessed = False

    while not guessed and tries != 0:
        choice = input('Take a guess: ').upper()
        if len(choice) == 1 and choice.isalpha():
            if choice in letters_guessed:
                print(f'{choice} has already been guessed')
            elif choice in word:
                print(f'Good {choice} is right!')
                letters_guessed.append(choice)
                word_as_list = list(blanks)
                indices = [i for i,letter in enumerate(word) if letter == choice]
                for x in indices:
                    word_as_list[x] = choice
                blanks = ''.join(word_as_list)
                if '-' not in blanks:
                    print('Congrats you got it right!!')
                    guessed = True
            else:
                tries-=1
                print('Oops you guessed it wrong')
                letters_guessed.append(choice)


        elif choice.isalpha():
            if choice == word:
                print(f'You Guessed it right')
                guessed = True
                words_guessed.append(choice)
                blanks = word
            else:
                words_guessed.append(choice)
                tries-=1
                print('Oops you guessed it wrong!')
        else:
            print('Invalid Guess')
        print(display_hangman(tries))
        print(blanks)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


continue_play = True
while continue_play:
    secret_word = get_word()
    print(secret_word)
    play_game(secret_word)
    play = input('You want to play again Y/N ?').upper()
    if play == 'N':
        continue_play = False
