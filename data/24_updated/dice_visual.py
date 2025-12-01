# Making a Histogram

# now that we have the data we want, we can generate a visualization in just a couple lines of code using Plotly Express:

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
fig = px.bar(x=poss_results, y=frequencies)
fig.show()

# We first import the plotly.express module, using the conventional alias px. We then use the px.bar() function to create a bar graph. In the simplest use of this function, we only need to pass a set of x-values and a set of y-values. Here the x-values are the possible results from rolling a single die, and the y-values are the frequencies for each possible result.

# The final line calls fig.show(), which tells Plotly to render the resulting chart as an HTML file and open that file in a new browser tab.

# This is a really simple chart, and it’s certainly not complete. But this is exactly how Plotly Express is meant to be used; you write a couple lines of code, look at the plot, and make sure it represents the data the way you want it to. If you like what you see, you can move on to customizing elements of the chart such as labels and styles. But if you want to explore other possible chart types, you can do so now, without having spent extra time on customization work. Feel free to try this now by changing px.bar() to something like px.scatter() or px.line(). You can find a full list of available chart types at https://plotly.com/python/plotly-express.

# This chart is dynamic and interactive. If you change the size of your browser window, the chart will resize to match the available space. If you hover over any of the bars, you’ll see a pop-up highlighting the specific data related to that bar.
