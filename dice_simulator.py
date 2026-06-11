# Simulates 100 dice rolls using NumPy
import numpy as np
dice_rolls = np.random.randint(1,7,100)
print(dice_rolls)
times_6_appear = dice_rolls[dice_rolls == 6]
print(times_6_appear.size)
avg_roll = dice_rolls.mean()
print(avg_roll)
highest_roll = dice_rolls.max()
print(highest_roll)
lowest_roll = dice_rolls.min()
print(lowest_roll)
times_1_appear = dice_rolls[dice_rolls == 1]
print(times_1_appear.size)
greater_than_4 = dice_rolls[dice_rolls > 4]
print(greater_than_4.size)
