"""A number-guessing game."""

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player


from random import randint

player_name = input("What is your name >> ")
print(f'Hello {player_name}.')
num = randint(1,100)
choice = int(input("Choose a number between 1-100 >> "))

while True:
    if choice != num:
        if choice > num:
            print("Your guess is too high.")
        elif choice < num:
            print("Your guess is too low.")
        choice = int(input("Please guess again >> "))
    else:
        print("Congrats!")
