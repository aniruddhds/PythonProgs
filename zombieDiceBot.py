import random

# Dice faces by color
DICE = {
    'green':   ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow':  ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red':     ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}

# Dice cup composition
DICE_CUP = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

def draw_dice(cup, num):
    """Draw num dice randomly from the cup without replacement."""
    drawn = []
    for i in range(num):
        if not cup:
            break
        die = random.choice(cup)
        cup.remove(die)
        drawn.append(die)
    return drawn

def roll_die(color):
    """Roll a single die of given color and return the face."""
    return random.choice(DICE[color])

def play_turn():
    cup = DICE_CUP.copy()
    brains = 0
    shotguns = 0
    footsteps_dice = []

    print(f"Your turn begins!")

    while True:
        # Prepare dice to roll: footsteps dice plus new dice to make 3 total
        dice_to_roll = footsteps_dice
        footsteps_dice = []
        dice_needed = 3 - len(dice_to_roll)
        dice_to_roll += draw_dice(cup, dice_needed)

        if not dice_to_roll:
            print("No dice left to draw or roll.")
            break

        print(f"Rolling dice: {dice_to_roll}")

        roll_results = []
        for die_color in dice_to_roll:
            face = roll_die(die_color)
            roll_results.append((die_color, face))

        for color, face in roll_results:
            print(f"  {color.capitalize()} die: {face}")

        # Count results
        brains_this_roll = sum(1 for _, face in roll_results if face == 'brain')
        shotguns_this_roll = sum(1 for _, face in roll_results if face == 'shotgun')
        footsteps_dice = [color for color, face in roll_results if face == 'footsteps']

        brains += brains_this_roll
        shotguns += shotguns_this_roll

        print(f"Brains: {brains_this_roll}, Shotguns: {shotguns_this_roll}")
        print(f"Total brains: {brains}, Total shotguns: {shotguns}")

        if shotguns >= 3:
            print(f"You have been shot. No brains scored this turn.")
            return 0
            break

        # Ask player whether to roll again
        while True:
            choice = input("Roll again? (y/n): ")
            if choice =='y' or choice=='n':
                break
            print("Please enter 'y' or 'n'.")

        if choice == 'n':
            print(f"Your game ends turn with {brains} brains.")
            return brains
            break

print("Welcome to Zombie Dice (Single Player)!")

total_score = 0
winning_score = 13

for i in range(1):
    turn_score = play_turn()
    total_score=total_score + turn_score # type: ignore
    print(f"Your total score: {total_score}")

print(f"You have {total_score} brains!")
