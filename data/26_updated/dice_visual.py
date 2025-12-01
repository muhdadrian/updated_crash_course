# Rolling Dice of Different Sizes

# Let’s create a six-sided die and a ten-sided die, and see what happens when we roll them 50,000 times:

import plotly.express as px
from dice import Dice

# Create a D6 and a D10
dice_1 = Dice()
dice_2 = Dice(10)  # 1

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"  # 2
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

# To make a D10, we pass the argument 10 when creating the second Die instance ❶ and change the first loop to simulate 50,000 rolls instead of 1,000. We change the title of the graph as well ❷.

# From the resulting chart, instead of one most likely result, there are five such results. This happens because there’s still only one way to roll the smallest value (1 and 1) and the largest value (6 and 10), but the smaller die limits the number of ways you can generate the middle numbers. There are six ways to roll a 7, 8, 9, 10, or 11, these are the most common results, and you’re equally likely to roll any one of them.

# Our ability to use Plotly to model the rolling of dice gives us considerable freedom in exploring this phenomenon. In just minutes, you can simulate a tremendous number of rolls using a large variety of dice.


# Saving Figures:
# When you have a figure you like, you can always save the chart as an HTML file through your browser. But you can also do so programmatically. To save your chart as an HTML file, replace the call to fig.show() with a call to fig.write_html():
# fig.write_html('dice_visual_d6d10.xhtml')

# The write_html() method requires one argument: the name of the file to write to. If you only provide a filename, the file will be saved in the same directory as the .py file. You can also call write_html() with a Path object, and write the output file anywhere you want on your system.
