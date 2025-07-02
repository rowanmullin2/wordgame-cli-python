import os, time, sys, random

class word_game:
  def __init__(self):
    self.attempts_left = 6
    self.word_was_guessed = False
    self.file = None
    self.words_solution = []
    self.words_guess = []
    self.word_to_guess = None
    self.old_guesses = []
    self.BORDER_LENGTH = 60

  # clears the screen
  def clear_screen(self):
    os.system('cls' if os.name == 'nt' else 'clear')

  # print border
  def print_border(self):
    print("*" * self.BORDER_LENGTH)

  # prints the text in the center of the screen
  def print_center(self, text):
    print(text.center(self.BORDER_LENGTH))

  # updates the words database from a file
  def update_data(self):
    try:
      self.file = open("words-solutions.txt", "r")
      if len(self.file.readline()) == 0:
        raise ValueError("File is empty")
      self.words_solution = self.file.read().splitlines()
      self.file = open("words-guesses.txt", "r")
      if len(self.file.readline()) == 0:
        raise ValueError("File is empty")
      self.words_guess = self.file.read().splitlines()
    except FileNotFoundError as e:
      print("File not found:", e.filename2)
    finally:
      if self.file is not None:
        self.file.close()

  def pick_word(self):
    self.word_to_guess = random.choice(self.words_solution).strip()

  # prints the start message for the game
  def print_start_msg(self):
    self.clear_screen()
    self.print_border()
    self.print_center("Welcome to wordl-erm I mean word game!")
    self.print_border()

  # prints the progress of the game
  def print_progress(self):
    print()
    self.print_border()
    self.print_center("Rules:")
    self.print_center("Type 'EXIT' to quit the game.")
    self.print_center("You can only guess 5 letter words.")
    self.print_center("Words must be Alphabetic characters only.")
    self.print_border()
    self.print_center("Info:")
    self.print_center(f"Attempts left: {self.attempts_left}")
    if self.attempts_left is not 6:
      self.print_border()
      self.print_center("Old guesses:")
      for i in self.old_guesses: self.print_center(i)
    self.print_border()

  # validates the input from the user.
  def validate_input(self, guess):
    validation_errors = (
    "Guess must be 5 letters long.",
    "Guess must be alphabetic characters only.",
    "Guess must be a valid word."
    )
    
    validation_checks = (
    (lambda guess: len(guess) == 5, validation_errors[0]),
    (lambda guess: guess.isalpha(), validation_errors[1]),
    (lambda guess: guess in self.words_guess, validation_errors[2])
    )

    # chcks if the guess is 'exit' to quit the game.
    if guess == "exit":
      self.clear_screen()
      self.print_border()
      self.print_center("Thanks for playing!")
      self.print_center(f"The word was: {self.word_to_guess}")
      self.print_border()
      sys.exit(0)

    has_errors = False
    # checks if the guess is valid.
    for check, error in validation_checks:
      if not check(guess):
        print(f"Invalid guess! {error}")
        has_errors = True

    if has_errors:
      time.sleep(3)
      self.clear_screen()
    else:
      # goes to the next step if the guess is valid.
      self.attempts_left -= 1
      score = self.check_guess(guess)
      self.print_response(score, guess)
      if score.count(2) == 5:
        self.word_was_guessed = True
      self.clear_screen()
    
  # Checks if the guess is correct.
  def check_guess(self, guess):
    response = []
    for i, char in enumerate(guess):
      match = False
      true_match = False
      for j, char_to_guess in enumerate(self.word_to_guess):
        if char == char_to_guess:
          match = True
          if i == j:
            true_match = True
            break
          else:
            true_match = False
      if true_match:
        response.append(2)
      elif match:
        response.append(1)
      else:
        response.append(0)
    return response
  
  # prints the response based on the guess.
  def print_response(self, response, guess):
    fancy_response = ""
    for i, v in enumerate(response):
      if v == 2:
        # Green for correct letter in correct position
        fancy_response += "\033[1;32m" + guess[i] + "\033[0m"  
      elif v == 1:
        # Yellow for correct letter in wrong position
        fancy_response += "\033[1;33m" + guess[i] + "\033[0m"
      else:
        # Red for incorrect letter
        fancy_response += "\033[1;31m" + guess[i] + "\033[0m"
    self.old_guesses.append(fancy_response)

  # prints the end message for the game.
  def print_end_message(self):
    self.print_border()
    if self.word_was_guessed:
      self.print_center(f"Congratulations! You guessed the word in {6 - self.attempts_left} attempts!")
    else:
      self.print_center("Sorry, you ran out of attempts.")
    self.print_border()
    self.print_center("You guessed:")
    for i in self.old_guesses: 
      print(i)
    self.print_center(f"The word was: {self.word_to_guess}")
    self.print_border()

# Main game loop
while True:
  # defines the round loop
  word_game_instance = word_game()
  word_game_instance.update_data()
  word_game_instance.pick_word()

  word_game_instance.print_start_msg()
  while word_game_instance.attempts_left > 0 and word_game_instance.word_was_guessed is False:
    word_game_instance.print_progress()
    # input from the user
    user_guess = input("Please enter your guess: ").lower().strip()
    word_game_instance.validate_input(user_guess)

  word_game_instance.print_end_message()
  input("Press any key to continue...")