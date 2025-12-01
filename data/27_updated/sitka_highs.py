# Make a folder called weather_data inside the folder where you’re saving this chapter’s programs. Copy the file sitka_weather_07- 2021_simple.csv into this new folder.

# Parsing the CSV File Headers
# Python’s csv module in the standard library parses the lines in a CSV file and allows us to quickly extract the values we’re interested in. Let’s start by examining the first line of the file, which contains a series of headers for the data. These headers tell us what kind of information the data holds:

import csv
from pathlib import Path

path = Path("weather_data/sitka_weather_07-2021_simple.csv")  # 1
lines = path.read_text().splitlines()

reader = csv.reader(lines)  # 2
header_row = next(reader)  # 3
print(header_row)

# We first import Path and the csv module. We then build a Path object that looks in the weather_data folder, and points to the specific weather data file we want to work with ❶. We read the file and chain the splitlines() method to get a list of all lines in the file, which we assign to lines.
# Next, we build a reader object ❷. This is an object that can be used to parse each line in the file. To make a reader object, call the function csv.reader() and pass it the list of lines from the CSV file.
# When given a reader object, the next() function returns the next line in the file, starting from the beginning of the file.

# Here we call next() only once, so we get the first line of the file, which contains the file headers ❸. We assign the data that’s returned to header_row. As you can see, header_row contains meaningful, weather-related headers that tell us what information each line of data holds:
# ['STATION', 'NAME', 'DATE', 'TAVG', 'TMAX', 'TMIN']

# The reader object processes the first line of comma- separated values in the file and stores each value as an item in a list. The header STATION represents the code for the weather station that recorded this data. The position of this header tells us that the first value in each line will be the weather station code. The NAME header indicates that the second value in each line is the name of the weather station that made the recording. The rest of the headers specify what kinds of information were recorded in each reading. The data we’re most interested in for now are the date (DATE), the high temperature (TMAX), and the low temperature (TMIN). This is a simple dataset that contains only temperature-related data. When you download your own weather data, you can choose to include a number of other measurements relating to wind speed, wind direction, and precipitation data.
