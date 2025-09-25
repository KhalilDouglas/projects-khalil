import random
playing = True
while (playing):
    secret_number = random.randint(1,25)
    guess_number = int(input("Guess a number: "))
    if (secret_number == guess_number):
        print("you got it")
    else:
        print("you got it Wrong")
    play_again = input ("do you want to continue?")
    if (play_again=="yes"):
        playing = True 
    else:
        playing = False
 