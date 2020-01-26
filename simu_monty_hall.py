import random
import matplotlib.pyplot as plt
import sys

num_changed_wins, num_unchanged_wins = 0, 0
prob_changes_wins, prob_unchanged_wins = [], []
NUM_DOORS = int(sys.argv[1])
NUM_SIMULATION = int(sys.argv[2])

for i in range(NUM_SIMULATION):
    door_new_car = random.randrange(NUM_DOORS)
    door_player_choice = random.randrange(NUM_DOORS)
    door_player_unchoice = [j for j in range(NUM_DOORS) if j != door_player_choice]

    if door_player_choice == door_new_car:
        door_monty_choice = random.choices(door_player_unchoice, k=NUM_DOORS-2)[0]
    else:
        door_player_unchoice_without_car = [j for j in door_player_unchoice if j != door_new_car] 
        door_monty_choice = random.choices(door_player_unchoice_without_car, k=NUM_DOORS-2)[0]

    door_another = [j for j in door_player_unchoice if j != door_monty_choice][0]

    if door_player_choice == door_new_car:
        num_unchanged_wins += 1
    elif door_another == door_new_car:
        num_changed_wins += 1

    prob_changes_wins.append(num_changed_wins / (i + 1))
    prob_unchanged_wins.append(num_unchanged_wins / (i + 1))
    
print('Number of Trials = ', NUM_SIMULATION)
print('num_changed_wins = ', num_changed_wins, ' prob_changes_wins = ', prob_changes_wins[-1])
print('num_unchanged_wins = ', num_unchanged_wins, ' prob_unchanged_wins', prob_unchanged_wins[-1])

plt.plot(prob_changes_wins, label='prob_changes_wins')
plt.plot(prob_unchanged_wins, label='prob_unchanged_wins')
plt.legend()
plt.show()
plt.savefig('simu_monty_hall.png')
