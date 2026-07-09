import random

jackport = random.randint(1, 100)
guess = int(input("Guess the number: "))
counter=1
while guess != jackport:
  if guess < jackport:
    print("Guess higher")
  else:
    print("Guess lower")
  guess = int(input("Let's guess the number again: "))
  counter+=1
print("Correct guess!")
print("You took",counter,"attempts:")