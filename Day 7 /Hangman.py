import random
import words
# Randomly choose a word from the list
chosen_word = random.choice(words.word_list)

# Add "_" for each word in the list
display = []
for letter in chosen_word:
    display += "_"

lives = 10
# Ask user the guess a letter in lowercase
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ")
    guess = guess.lower()

    # Check if the letter is in the word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{" ".join(display)}")
    print(f"You have {lives} lives")

    if "_" not in display:
        end_of_game = True
        print("You win!")
