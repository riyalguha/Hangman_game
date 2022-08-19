import random
from replit import clear
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
import hangman_art
word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")

while display.count("_")>=1:
    guess = input("Guess a letter: ").lower()
    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    if guess in display:
        print(f"The Letter {guess} has already been guessed")  
    for n in range(0,len(chosen_word)):
      if chosen_word[n]==guess:
        display[n]=guess
    
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"The Letter {guess} was not in the word")
    if lives==0:
      print("You Lose")
      print(hangman_art.stages[lives])
      break

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if display.count("_")==0:
      print("You Have Won")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
