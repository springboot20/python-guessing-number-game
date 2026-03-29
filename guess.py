import random

# TODO: 
## user enter a number to try guess
## generate the random number
## check for user input to match the randomly guessed number

def request_user_response() -> int:
    """Prompt the user for a number, re-prompting on invalid input."""
    while True: 
       try:
          return int(input("Guess a number between 1 and 20: "))
    
       except ValueError:
          print("\nInvalid input! Please enter a whole number.")

def main(): 
  randomly_generated_number = random.randint(0, 20)
  max_attempt = 3

  print("# " * 40)
  print("       🎯 Number Guessing Game")
  print("# " * 40, "\n")
  print(f"NOTE: You have a maximum of ({max_attempt}) attempts.\n")

  while max_attempt != 0:
    user_input = request_user_response()

    if user_input == randomly_generated_number:
      max_attempt = 0
      print(f"🎉 Congratulations! You guessed the number right: {randomly_generated_number}\n")
    else:
      max_attempt -= 1
      if max_attempt > 0:
         print(f"\nWrong guess! Attempts remaining: ({max_attempt})\n")
      else:
        print(f"Out of attempts! The number was {randomly_generated_number}\n")

  print("# " * 40)

if __name__ ==  "__main__":
  main()
