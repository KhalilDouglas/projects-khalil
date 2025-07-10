import random
def lucky_guess(guess,range):
  lucky_guess = random.randint(1,range)
for attempt in range (1,6):
  if guess== lucky_guess:
    print("success")
else:
    print("Try again")
guess= int(input("Take another guess"))
lucky_guess(4,50) 