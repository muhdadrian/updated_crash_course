# Customizing the Plot

# Now that we know we have the correct kind of plot and our data is being represented accurately, we can focus on adding the appropriate labels and styles for the chart.

# The first way to customize a plot with Plotly is to use some optional parameters in the initial call that generates the plot, in this case, px.bar(). Here’s how to add an overall title and a label for each axis:

import plotly.express as px
from dice import Dice

# Create a D6
dice = Dice()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, dice.num_sides + 1)  # 2
for value in poss_results:
    frequency = results.count(value)  # 3
    frequencies.append(frequency)  # 4

# Visualize the results.
title = "Results of Rolling One D6 1,000 Times"  # 1
labels = {"x": "Result", "y": "Frequency of Result"}  # 2
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

# We first define the title that we want, here assigned to title ❶. To define axis labels, we write a dictionary ❷. The keys in the dictionary refer to the labels we want to customize, and the values are the custom labels we want to use. Here we give the x-axis the label Result and the y-axis the label Frequency of Result. The call to px.bar() now includes the optional arguments title and labels.
