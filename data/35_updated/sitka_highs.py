# Shading an Area in the Chart

# Having added two data series, we can now examine the range of temperatures for each day. Let’s add a finishing touch to the graph by using shading to show the range between each day’s high and low temperatures. To do so, we’ll use the fill_between() method, which takes a series of x-values and two series of y-values and fills the space between the two series of y-values:


import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)  # 1
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)  # 2
# ax.plot(dates, highs, color="red")
# ax.plot(dates, lows, color="blue")

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

# The alpha argument controls a color’s transparency ❶. An alpha value of 0 is completely transparent, and a value of 1 (the default) is completely opaque. By setting alpha to 0.5, we make the red and blue plot lines appear lighter.
# We pass fill_between() the list dates for the x-values and then the two y-value series highs and lows ❷. The facecolor argument determines the color of the shaded region; we give it a low alpha value of 0.1 so the filled region connects the two data series without distracting from the information they represent.

# The chart shows the plot with the shaded region between the highs and lows.

# The shading helps make the range between the two datasets immediately apparent.
