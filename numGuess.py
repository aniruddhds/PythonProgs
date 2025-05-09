import random as ran
comp=ran.randint(1,10)
print("Guess the number!")

while True:
    choice=input("Enter your choice: ")
    choice=int(choice)
    if choice==comp:
        print("Good guess.")
        print("Congrats. You win!")
        break
    else:
        print("Nope. Guess again.")
        print("Hint: It's between 1 and 10")
        continue