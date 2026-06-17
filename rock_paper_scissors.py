import random
print("Welcome to Rock Paper Scissors!")
print("let's see who's gonna win!")
user_score = 0
computer_score = 0
choices = ["rock","paper","scissors"]
while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice!Try again.")
        continue
    computer = random.choice(choices)
    print("Computer chose:",computer)
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"Score -> You: {user_score} | Computer: {computer_score}")
    play_again = input("Do you want to play again?(yes/no): ").lower()
    if play_again != "yes":
        break
print("\nFinal Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("The game ended in a tie!")