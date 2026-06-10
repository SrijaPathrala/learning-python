import random
secret_number = random.randint(1,100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
while True:
    try:
        guess= int(input("Enter your guess: "))
        attempts+=1
        if guess<secret_number:
            print("Too low,try again!")
        elif guess>secret_number:
            print("Too high,try again!")
        else:
             print(f"Congratulations! You guessed it in {attempts} attempts.")
             break 
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

if attempts <= 5:
    print("Excellent guessing!")
elif attempts <= 10:
    print("Good job!")
else:
    print("You got it eventually!")
    
    