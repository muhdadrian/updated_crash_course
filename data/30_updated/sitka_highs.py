# Plotting Data in a Temperature Chart

# To visualize the temperature data we have, we’ll first create a simple plot of the daily highs using Matplotlib, as shown here:

import csv
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# Plot the high temperatures.
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(highs, color="red")  # 1

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)  # 2
ax.set_xlabel("", fontsize=16)  # 3
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# We pass the list of highs to plot() and pass color='red' to plot the points in red ❶. (We’ll plot the highs in red and the lows in blue.) We then specify a few other formatting details, such as the title, font size, and labels ❷, just as we did in previous chapter. Because we have yet to add the dates, we won’t label the x-axis, but ax.set_xlabel() does modify the font size to make the default labels more readable ❸. The chart shows the resulting plot: a simple line graph of the high temperatures for July 2021 in Sitka, Alaska.
