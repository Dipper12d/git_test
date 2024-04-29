import random

guess = secret = count = 0
carry_on = True
print("=" * 40)
print("Guessing Game")
print("Can you guess the secret number?")
print("Select a number between 1 to 100")
print("=" * 40)
secret = random.randint(1, 9999)
while carry_on := True:
    guess = int(input("Please select a number between 1 to 9999:"))
    if guess == secret:
        count += 1
        print(f"Congrats! You guessed {secret} in {count} tries")
        carry_on = False
        break
    if guess < secret:
        count += 1
        print("Too low, Try again")
    else:
        count += 1
        print("Too high, Try again")
print("Goodbye")
