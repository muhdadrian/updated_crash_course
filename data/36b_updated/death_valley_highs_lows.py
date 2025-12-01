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
    try:  # 1
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")  # 2
    else:  # 3
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
# ax.plot(dates, highs, color="red")
# ax.plot(dates, lows, color="blue")

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"  # 4
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

# Each time we examine a row, we try to extract the date and the high and low temperature ❶. If any data is missing, Python will raise a ValueError and we handle it by printing an error message that includes the date of the missing data ❷. After printing the error, the loop will continue processing the next row. If all data for a date is retrieved without error, the else block will run and the data will be appended to the appropriate lists ❸. Because we’re plotting information for a new location, we update the title to include the location on the plot, and we use a smaller font size to accommodate the longer title ❹.
# When you run death_valley_highs_lows.py now, you’ll see that only one date had missing data:
# Missing data for 2021-05-04 00:00:00

# Because the error is handled appropriately, our code is able to generate a plot, which skips over the missing data. The chart shows the resulting plot.
# Comparing this graph to the Sitka graph, we can see that Death Valley is warmer overall than southeast Alaska, as we expect. Also, the range of temperatures each day is greater in the desert. The height of the shaded region makes this clear.

# Many datasets you work with will have missing, improperly formatted, or incorrect data. You can use the tools you learned in the first half of this book to handle these situations. Here we used a try-except-else block to handle missing data. Sometimes you’ll use continue to skip over some data, or use remove() or del to eliminate some data after it’s been extracted. Use any approach that works, as long as the result is a meaningful, accurate visualization.
