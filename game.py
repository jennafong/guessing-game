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

while True:
    try:
        choice = int(input("Choose a number between 1-100 >> "))
        if choice > 0:
            break
    except ValueError:
            print("lol, nice try. Please enter an integer.")
            

while True:
    if choice != num:
        if choice >= 100 or choice <= 0:
            print("lol, you're funny. Enter a valid number.")
        elif choice > num:
            print("Your guess is too high.")
        elif choice < num:
            print("Your guess is too low.")
        
        try:
            choice = int(input("Please guess again >> "))
            if choice > 0:
                continue
        except ValueError:
            print("lol, nice try. Please enter an integer.")

    else:
        print("Congrats!")
        break
