'''the rules!!!
rock beats scissors
scissors beats paper
paper beats rock'''
#if comparison condition is true, user wins, or else, cmp wins
# rock=1 paper=2 scissors=3

import random
#take user input,convert choice, display
usrIn=input("enter your choice (r(ock),p(aper),s(cissors)): ")
if usrIn=='r':
    usr=1
    print("You have chosen ROCK.")
elif usrIn=='p':
    usr=2
    print("You have chosen PAPER.")
else:
    usr=3
    print("You have chosen SCISSORS.")

#generate comp choice, display
cmp=random.randint(1,3)
if cmp==1:
    print("Computer chooses ROCK.")
elif cmp==2:
    print("Computer chooses PAPER.")
else:
    print("Computer chooses SCISSORS.")
    
#the game logic
if cmp>usr:
    print("Computer WINS!")
elif cmp<usr:
    print("You win!.")
else:
    print("It's a draw!")

print("GOOD GAME!")