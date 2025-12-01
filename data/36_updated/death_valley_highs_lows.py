# Error Checking

# We should be able to run the sitka_highs_lows.py code using data for any location. But some weather stations collect different data than others, and some occasionally malfunction and fail to collect some of the data they’re supposed to. Missing data can result in exceptions that crash our programs, unless we handle them properly.

# For example, let’s see what happens when we attempt to generate a temperature plot for Death Valley, California. Copy the file death_valley_2021_simple.csv to the folder where you’re storing the data for this chapter’s programs.

# First, let’s run the code to see the headers that are included in this data file:

import csv
from pathlib import Path

path = Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Here’s the output:
#   0 STATION
#   1 NAME
#   2 DATE
#   3 TMAX
#   4 TMIN
#   5 TOBS

# The date is in the same position, at index 2. But the high and low temperatures are at indexes 3 and 4, so we’ll need to change the indexes in our code to reflect these new positions. Instead of including an average temperature reading for the day, this station includes TOBS, a reading for a specific observation time.

# Change sitka_highs_lows.py to generate a graph for Death Valley using the indexes we just noted, and see what happens at 36a_updated
