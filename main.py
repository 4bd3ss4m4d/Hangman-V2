# The Hangman Game

import random
import HangmanASCIIArt

def randomWord(WordsList):
    maxWordsListIndex = len(WordsList) - 1
    random_index = random.randint(0, maxWordsListIndex)
    chosen_word = WordsList[random_index]
    return chosen_word


def get_index(user_char, wordCharsList):
    indexes = []
    for i in range(len(wordCharsList)):
        if wordCharsList[i] == user_char:
            indexes.append(i)
    return indexes


def main():
    play_again = 'y'

    while play_again == 'y':

        # Printing the Welcome to the Hangman game message.
        welcome_message = "\nWelcome to the Hangman Game!\n"
        print(welcome_message)

        # list of the Hangman life cycle
        life_cycle = [HangmanASCIIArt.h1, HangmanASCIIArt.h2, HangmanASCIIArt.h3, HangmanASCIIArt.h4, HangmanASCIIArt.h5,
                      HangmanASCIIArt.h6, HangmanASCIIArt.h7]
        # Print the first Hangman life cycle
        print(life_cycle[0] + '\n')

        # Print rule of the game message
        game_rule = "Try to guess the characters of the word before the Hangman dies!\n"
        print(game_rule)

        # List of words
        words = ["Book", "School", "Million", "Billion"]
        word = randomWord(words).lower()

        # Creating a list containing blank spaces equal to the random word chosen
        wordCharsList = list(word)
        blankSpaces = []
        for i in wordCharsList:
            blankSpaces.append('X')
        # Add a point to the end of the blank spaces list
        blankSpaces.append('.')
        # Printing the list of blank spaces as a one string
        print("".join(blankSpaces))
        print(f"The word you need to guess contains {len(word)} words!")

        life_counter = 0

        word_with_point = word + '.'
        while life_counter < 6:
            user_chars = "".join(blankSpaces)
            if user_chars.lower() == word_with_point.lower():
                winning_message = "Congrats! You've saved the Hangman\n"
                created_by = "Created by 4bd3ss4m4d\n"
                print(winning_message)
                print(created_by)
                break

            # Get user's input
            user_char = input('').lower()

            # Check whether user's char input is in the word
            if user_char in wordCharsList:
                # Call the get_indexes function
                char_indexes = get_index(user_char, wordCharsList)
                # Replace blank chars with char chosen by the user
                for index in char_indexes:
                    blankSpaces[index] = user_char
                print("".join(blankSpaces).capitalize())

            # Check whether user's char input is not in the word
            elif user_char not in wordCharsList:
                if life_counter >= 5:
                    print(life_cycle[6])
                    print("The Hangman died! Shame on you")
                    break
                else:
                    print(life_cycle[life_counter + 1])
                    print("Careful! The man in dying!!")
                    print("Try again!\n")
                    print("".join(blankSpaces).capitalize())
                    life_counter += 1
        play_again = input("Type 'y' to play again or 'q' to quit: ").lower()
        if play_again == 'y':
            life_counter = 0

main()

