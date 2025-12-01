# Representing Magnitudes

# A map of earthquake activity should show the magnitude of each earthquake. We can also include more data, now that we know the data is being plotted correctly.

import json
from pathlib import Path

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title)
fig.show()

# We load the file eq_data_30_day_m1.geojson, to include a full 30 days’ worth of earthquake activity. We also use the size argument in the px.scatter_geo() call, which specifies how the points on the map will be sized. We pass the list mags to size, so earthquakes with a higher magnitude will show up as larger points on the map.

# The resulting map is shown in the chart. Earthquakes usually occur near tectonic plate boundaries, and the longer period of earthquake activity included in this map reveals the exact locations of these boundaries.

# The map now shows the magnitude of all earthquakes in the last 30 days.

# This map is better, but it’s still difficult to pick out which points represent the most significant earthquakes. We can improve this further by using color to represent magnitudes as well.
