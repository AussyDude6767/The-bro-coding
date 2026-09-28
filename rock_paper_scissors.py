import random
print()
print("Welcome to the Rock, Paper, Scissors Online Edition!")
print()
moves = ["rock", "paper", "scissors"]
yourWins = 0
AIWins = 0

try:
    while True:
        go = input("Continue? (yes/no): ")
        print()

        if go == "yes":
            move = input("Enter your move (rock/paper/scissors): ")
            AIMove = random.choice(moves)
            if move == "rock" or move == "paper" or move == "scissors":
                print(f"AI's move: {AIMove}")
                if AIMove == "rock" and move == "paper":
                    print("You win!") ; yourWins += 1
                    print()
                elif AIMove == "paper" and move == "rock":
                    print("AI wins!") ; AIWins += 1
                    print()
                elif AIMove == "paper" and move == "scissors":
                    print("You win!") ; yourWins +=1 
                    print()
                elif AIMove == "scissors" and move == "paper":
                    print("AI wins!") ; AIWins += 1
                    print()
                elif AIMove == "scissors" and move == "rock":
                    print("You win!") ; yourWins += 1
                    print()
                elif AIMove == "rock" and move == "scissors":
                    print("AI wins!") ; AIWins += 1
                    print()
                else:
                    print("Tie!")
                    print()
            else:
                print("Invalid input - please try again (case sensitive)")
                print()

        elif go == "no":
            score = input("Would you like to see the score? (yes/no): ")
            if score == "yes":
                print(f"Your wins: {yourWins}")
                print(f"AI's wins: {AIWins}")
            else:
                print("Okay!")
            print()
            print("Thank you for playing the Rock, Paper, Scissors Online Edition! 👋")
            print()
            break

        else:
            print("Invalid input - please try again (case sensitive)")
            print()
        
except:
    print()
    print("Error - please try again later")
    print()
