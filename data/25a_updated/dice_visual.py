# Further Customizations

# There’s one issue that we should address with the plot we just generated. Now that there are 11 bars, the default layout settings for the x-axis leave some of the bars unlabeled. While the default settings work well for most visualizations, this chart would look better with all of the bars labeled.

# Plotly has an update_layout() method that can be used to make a wide variety of updates to a figure after it’s been created. Here’s how to tell Plotly to give each bar its own label:

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
# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

# The update_layout() method acts on the fig object, which represents the overall chart. Here we use the xaxis_dtick argument, which specifies the distance between tick marks on the x-axis. We set that spacing to 1, so that every bar is labeled. When you run dice_visual.py again, you should see a label on each bar.
