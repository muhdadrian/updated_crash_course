# Printing the Headers and Their Positions

# To make it easier to understand the file header data, let’s print each header and its position in the list:

import csv
from pathlib import Path

path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# The enumerate() function returns both the index of each item and the value of each item as you loop through a list. (Note that we’ve removed the line print(header_row) in favor of this more detailed version.)
# Here’s the output showing the index of each header:
#    0 STATION
#    1 NAME
#    2 DATE
#    3 TAVG
#    4 TMAX
#    5 TMIN

# We can see that the dates and their high temperatures are stored in columns 2 and 4. To explore this data, we’ll process each row of data in sitka_weather_07- 2021_simple.csv and extract the values with the indexes 2 and 4.
