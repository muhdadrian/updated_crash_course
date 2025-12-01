# Rolling Two Dice

# Rolling two dice results in larger numbers and a different distribution of results. Let’s modify our code to create two D6 dice to simulate the way we roll a pair of dice. Each time we roll the pair, we’ll add the two numbers (one from each die) and store the sum in results.

import plotly.express as px
from dice import Dice

# Create a D6
dice_1 = Dice()
dice_2 = Dice()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()  # 1
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides  # 2
poss_results = range(2, max_result + 1)  # 3
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

# After creating two instances of Die, we roll the dice and calculate the sum of the two dice for each roll ❶. The smallest possible result (2) is the sum of the smallest number on each die. The largest possible result (12) is the sum of the largest number on each die, which we assign to max_result ❷. The variable max_result makes the code for generating poss_results much easier to read ❸. We could have written range(2, 13), but this would work only for two D6 dice. When modeling real-world situations, it’s best to write code that can easily model a variety of situations. This code allows us to simulate rolling a pair of dice with any number of sides.

# The graph shows the approximate distribution of results you’re likely to get when you roll a pair of D6 dice. As you can see, you’re least likely to roll a 2 or a 12 and most likely to roll a 7. This happens because there are six ways to roll a 7: 1 and 6, 2 and 5, 3 and 4, 4 and 3, 5 and 2, and 6 and 1.
