# Plotting a Second Data Series

# We can make our graph even more useful by including the low temperatures. We need to extract the low temperatures from the data file and then add them to our graph, as shown here:

import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []  # 1
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])  # 2
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")  # 3

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)  # 4
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

# We add the empty list lows to hold low temperatures ❶, and then we extract and store the low temperature for each date from the sixth position in each row (row[5]) ❷. We add a call to plot() for the low temperatures and color these values blue ❸. Finally, we update the title ❹.

# The chart shows two data series on the same plot
