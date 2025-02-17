import random
random_number=random.randint(1,100)
attempts=0
while attempts<11:
    guess=int(input("Try to guess: "))
    if guess>random_number:
        print("Too high!")
    elif guess<random_number:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
    attempts+=1
    if attempts==10:
        print("You lost. Want to play again? ")
        game_restart=input()
        if game_restart=='y' or game_restart=='Y' or game_restart=='YES' or game_restart=='yes' or game_restart=='ok':
            attempts=0