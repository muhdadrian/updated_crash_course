# Extracting Location Data

# The location data for each earthquake is stored under the key "geometry". Inside the geometry dictionary is a "coordinates" key, and the first two values in this list are the longitude and latitude. Here’s how we’ll pull this data:

import json
from pathlib import Path

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]  # 1
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:5])
print(lats[:5])

# We make empty lists for the longitudes and latitudes. The code eq_dict['geometry'] accesses the dictionary representing the geometry element of the earthquake ❶. The second key, 'coordinates', pulls the list of values associated with 'coordinates'. Finally, the 0 index asks for the first value in the list of coordinates, which corresponds to an earthquake’s longitude.

# When we print the first 5 longitudes and latitudes, the output shows that we’re pulling the correct data:
#    [1.6, 1.6, 2.2, 3.7, 2.92000008, 1.4, 4.6, 4.5, 1.9, 1.8]
#    [-150.7585, -153.4716, -148.7531, -159.6267, -155.248336791992]
#    [61.7591, 59.3152, 63.1633, 54.5612, 18.7551670074463]
# With this data, we can move on to mapping each earthquake.
