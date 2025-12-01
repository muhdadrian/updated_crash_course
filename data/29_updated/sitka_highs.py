# Extracting and Reading Data

# Now that we know which columns of data we need, let’s read in some of that data. First, we’ll read in the high temperature for each day:


import csv
from pathlib import Path

path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = []  # 1
for row in reader:  # 2
    high = int(row[4])  # 3
    highs.append(high)

print(highs)

# We make an empty list called highs ❶ and then loop through the remaining rows in the file ❷. The reader object continues from where it left off in the CSV file and automatically returns each line following its current position. Because we’ve already read the header row, the loop will begin at the second line where the actual data begins. On each pass through the loop we pull the data from index 4, corresponding to the header TMAX, and assign it to the variable high ❸. We use the int() function to convert the data, which is stored as a string, to a numerical format so we can use it. We then append this value to highs.

# The following listing shows the data now stored in highs:
# [61, 60, 66, 60, 65, 59, 58, 58, 57, 60, 60, 60, 57, 58, 60, 61, 63, 63, 70, 64, 59, 63, 61, 58, 59, 64, 62, 70, 70, 73, 66]

# We’ve extracted the high temperature for each date and stored each value in a list. Now let’s create a visualization of this data at the next folder.
