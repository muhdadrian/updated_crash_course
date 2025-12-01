# Plotting Dates
# We can improve our plot by extracting dates for the daily high temperature readings, and using these dates on the x- axis:

import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs = [], []  # 1

for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")  # 2
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Plot the high temperatures.
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")  # 3

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()  # 4
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

# We create two empty lists to store the dates and high temperatures from the file ❶. We then convert the data containing the date information (row[2]) to a datetime object ❷ and append it to dates. We pass the dates and the high temperature values to plot() ❸. The call to fig.autofmt_xdate() ❹ draws the date labels diagonally to prevent them from overlapping. The chart shows the improved graph.

# The graph is more meaningful, now that it has dates on the x-axis.
