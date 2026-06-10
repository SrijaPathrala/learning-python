print("Welcome to Python quiz challenge!")
print("Let's Start!")
score=0
print('''1. Which function is used to take input from the user?
a) print()
b) input()
c) int()
d) str()''')
answer1= input("Enter your answer: ").lower()
if answer1=='b':
    print("Correct")
    score+=1
else:
    print("Wrong!")
print('''2. Which keyword is used for a loop that repeats while a condition is true?
a) for
b) repeat
c) while
d) loop''')
answer2=input("Enter your answer: ").lower()
if answer2=='c':
    print("Correct")
    score+=1
else:
    print("Wrong!")
print('''3. What does len("Python") return?
a) 5
b) 6
c) 7
d) Error''')
answer3=input("Enter your answer: ").lower()
if answer3=='b':
    print("Correct")
    score+=1
else:
    print("Wrong!")
print("Score:",score)
print(f"Your final score is {score}/3")
if score == 3:
    print("Yay! You are a Python Pro!")
elif score == 2:
    print("Great Job!")
else:
    print("Keep Practicing!")
