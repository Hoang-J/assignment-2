# === PROBLEM 0 ===
# ~ Scenario ~
# You are a software engineer at Nintendo. Your task is to
# create a new game called "Guess That Number" where the
# user will try to guess what number the computer is
# thinking of.
#
# ~ Success Criteria ~
# When the script is run, the computer will randomly select
# a number between 1 and 5. Then, the user will be prompted
# to guess what number the computer is "thinking". If the
# user is correct, display a victory message. Else, display
# a lose message with the number the computer "thought" of.
#
# ~ Example ~
# Scenario 1
#   The computer selects the number 1.
#   Input: 1
#   Output: You win!
# Scenario 2
#   The computer selects the number 4.
#   Input: 3
#   Output: You lose! I was thinking of 4.

# TODO write your code here


import random

number = [1, 2, 3, 4, 5]

while True:
    computer_answer = number[random.randint(0, len(number)-1)]
    player_guess = int(input('What number between 1 and 5 am I thinking of? '))

    while True:
        if computer_answer == player_guess:
            print('Yes! You got it!')
            break
        else:
            ca_string = str(computer_answer)
            print('Wrong! It was', ca_string + '.')
            break



