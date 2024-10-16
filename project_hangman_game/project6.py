#HANGMAN GAME

import random
import hangman_words
import hangman_art

print("\n************WELCOME TO************")
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("\n=> Word to guess: " + placeholder+"\n")

game_over = False
correct_letters = []

lives = 6
while not game_over:
    print(f"\n*************** You have {lives} left *******************\n")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"\n## You already guessed the letter: '{guess}' ##")
        continue

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("\n=> Word to guess: " + display)


    if guess not in chosen_word:


        print(f"You guessed '{guess}'. That's not in the word.\n---You lost a life.---")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"\nIt was '{chosen_word}!'\n")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
