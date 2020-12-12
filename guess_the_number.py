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


if __name__ == "__main__":
    guess_user(10)
