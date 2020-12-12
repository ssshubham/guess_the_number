import random


def guess_user(x):
    low = 1
    high = x
    random_number = random.randint(low, high)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between {low} and {high}!!"))
        if guess < random_number:
            print("Sorry wrong guess !! Too low ")
        elif guess > random_number:
            print("Sorry wrong guess !! Too high ")
    print("Yay congrats !! You guessed right answer ")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = 0
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is the number {guess} ?")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay, The computer guessed your number {guess} correctly !!")


if __name__ == "__main__":
    # guess_user(10)
    computer_guess(10)
