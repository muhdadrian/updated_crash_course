# Extracting Magnitudes
#
# We can loop through the list containing data about each earthquake, and extract any information we want. Let’s pull out the magnitude of each earthquake:

import json
from pathlib import Path

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags = []  # 1
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]  # 2
    mags.append(mag)

print(mags[:10])

# We make an empty list to store the magnitudes, and then loop through the list all_eq_dicts ❶. Inside this loop, each earthquake is represented by the dictionary eq_dict. Each earthquake’s magnitude is stored in the 'properties' section of this dictionary, under the key 'mag' ❷. We store each magnitude in the variable mag and then append it to the list mags.

# We print the first 10 magnitudes, so we can see whether we’re getting the correct data:
#   [1.6, 1.6, 2.2, 3.7, 2.92000008, 1.4, 4.6, 4.5, 1.9, 1.8]
# Next, we’ll pull the location data for each earthquake, and then we can make a map of the earthquakes.
