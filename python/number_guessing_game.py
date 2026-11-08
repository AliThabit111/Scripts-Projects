"""Number Guessing Game (Python): guess the secret number between 1 and 20."""
import random

LOW, HIGH = 1, 20


def main() -> None:
    secret = random.randint(LOW, HIGH)
    tries = 0
    guess = None

    print(f"I'm thinking of a number between {LOW} and {HIGH}")

    while guess != secret:
        text = input("Take a guess: ")
        try:
            guess = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        tries += 1

        if guess < LOW or guess > HIGH:
            print("That number is out of range. Try again.")
        elif guess < secret:
            print("Too low, try again.")
        elif guess > secret:
            print("Too high, try again.")
        else:
            print("You got it in", tries, "tries!")


if __name__ == "__main__":
    main()
