import random

print()
print("Welcome to the Guess the Number game!")
print()

tries=(0)

try:
    number = random.randint(1, 1000)
    while True:
        guess = int(input("Enter your guess (range is 1 - 1000 inclusive): "))
        if guess >= 1 and guess <= 1000:
            if guess > number:
                print("The number is lower!")
                print()
                tries += 1
            elif guess < number:
                print("The number is higher!")
                print()
                tries += 1
            elif guess == number:
                print("You got the number!")
                print()
                score = input("Would you like to see how many tries it took? (yes/no): ")
                if score == "yes":
                    print(f"Attempts: {tries}")
                else:
                    print("Okay!")
                print()
                print("Thank you for playing the Guess the Number game! See you next time! 👋")
                print()
                break

        else:
            print("Invalid input - please try again (case sensitive)")
            print()

except:
    print()
    print("Error - please try again later")
    print()
