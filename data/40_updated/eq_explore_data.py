# Making a List of All Earthquakes

# First, we’ll make a list that contains all the information about every earthquake that occurred.

import json
from pathlib import Path

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

# We take the data associated with the key 'features' in the all_eq_data dictionary, and assign it to all_eq_dicts. We know this file contains records of 160 earthquakes, and the output verifies that we’ve captured all the earthquakes in the file:
# 160

# Notice how short this code is. The neatly formatted file readable_eq_data.json has over 6,000 lines. But in just a few lines, we can read through all that data and store it in a Python list. Next, we’ll pull the magnitudes from each earthquake.
