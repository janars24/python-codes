import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
lives = 6

chosen_word = random.choice(word_list)

nr_dashes = ""
lengthOfWord = len(chosen_word)
for dash in range(lengthOfWord):
    nr_dashes += "-"
print("Welcome to Hangman Game!")
print(f"Word to guess is shown below\n{nr_dashes}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"Letter you guessed is '{guess}'")
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not

    if guess in correct_letters:
        print(f"You already guessed {guess} guess a different letter")
    display = ""

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += "-"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "-" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
    print(f"No of lives left '{lives}'")