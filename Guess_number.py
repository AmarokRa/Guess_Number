
from random import randint
from Guess_number_art import logo 


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function qui permet de vérifier si la proposition faite par le joueur et plus haute ou plus basse que la réponse à deviner.
def check_low_high(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1

  elif guess < answer:
    print("Too low.")
    return turns - 1

  else:
    print(f"You got it! The answer was {answer}.")

#Function qui permet de choisir sa difficulté.
def set_difficulty():

  choose_diff = input("choose a difficulty. Type 'easy' or 'hard': \n")
  if choose_diff == 'easy': 
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

#Function qui permet de lancer le jeu et d'y jouer.
def game():
  print(logo)
#L'ordinateur choisie un nombre entre 1 et 100.
  print("welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  
  turns = set_difficulty()
  
  guess = 0

#  Boucle qui va permettre de répéter la mécanique de gameplay de base. 
  while guess != answer:
    print(f"You have {turns} remaining to guess the number.")

#Le joueur écrit le nombre auquel il pense.
    guess = int(input("Make a guess: "))

    turn = check_low_high(guess, answer, turns)
#Si le nombre de tentative tombe à 0 alors le joueur à perdu.    
    if turn == 0:
      print("You've run out of guesses you lose.")
      return
#Si la proposition est différente de la réponse, alors tu peux retenter      
    elif guess != answer:
      print("Guess again.")

def main():
  while True:
    game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again != 'y':
      break

main()