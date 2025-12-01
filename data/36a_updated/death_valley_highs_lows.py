import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[3])
    low = int(row[4])
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

# We update the program to read from the Death Valley data file, and we change the indexes to correspond to this file’s TMAX and TMIN positions.
# When we run the program, we get an error:

#    Traceback (most recent call last):
#      File "death_valley_highs_lows.py", line 17, in <module>
# high = int(row[3])
# ❶ ValueError: invalid literal for int() with base 10: ''

# The traceback tells us that Python can’t process the high temperature for one of the dates because it can’t turn an empty string ('') into an integer ❶. Rather than looking through the data to find out which reading is missing, we’ll just handle cases of missing data directly.
# We’ll run error-checking code when the values are being read from the CSV file to handle exceptions that might arise.
# how to do, go to 36b_updated
