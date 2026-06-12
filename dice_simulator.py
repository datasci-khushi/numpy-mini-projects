# Simulates 100 dice rolls using NumPy
import numpy as np
dice_rolls = np.random.randint(1,7,100)
print("Simulated Dice Rolls (n=100) =", dice_rolls)
times_6_appear = dice_rolls[dice_rolls == 6]
print("Frequency of 6 =", times_6_appear.size)
avg_roll = dice_rolls.mean()
print("Mean =", avg_roll)
highest_roll = dice_rolls.max()
print("Max Roll =", highest_roll)
lowest_roll = dice_rolls.min()
print("Min Roll =", lowest_roll)
times_1_appear = dice_rolls[dice_rolls == 1]
print("Frequency of 1 =", times_1_appear.size)
greater_than_4 = dice_rolls[dice_rolls > 4]
print("Rolls > 4 =", greater_than_4.size)
