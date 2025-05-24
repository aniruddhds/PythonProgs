import random

def generate_flips(num_flips):
    flips = []
    for _ in range(num_flips):
        flip_result = random.randint(0, 1)
        if flip_result == 0:
            flips.append('H')
        else:
            flips.append('T')
    return flips


def has_streak(flips, streak_length=6):
    """Check if the list contains a streak of streak_length heads or tails."""
    count = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            count += 1
            if count == streak_length:
                return True
        else:
            count = 1
    return False

def run_experiments(num_experiments, num_flips, streak_length=6):
    streak_count = 0
    for _ in range(num_experiments):
        flips = generate_flips(num_flips)
        if has_streak(flips, streak_length):
            streak_count += 1
    percentage = (streak_count / num_experiments) * 100
    print(f"Out of {num_experiments} experiments, {streak_count} contained a streak of {streak_length}.")
    print(f"Percentage: {percentage:.2f}%")

NUM_EXPERIMENTS = 10000
NUM_FLIPS = 100  # Number of flips per experiment
STREAK_LENGTH = 6

run_experiments(NUM_EXPERIMENTS, NUM_FLIPS, STREAK_LENGTH)
